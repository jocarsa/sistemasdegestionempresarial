<?php
// base/graficas_ui.php
require_once __DIR__ . "/../util/helpers.php";
require_once __DIR__ . "/../util/db.php";
require_once __DIR__ . "/../util/crud.php";

/**
 * Heurística "columna repetible/discreta":
 * - Excluye PK y columnas tipo id/fk típicas.
 * - Cuenta filas totales y distintos (no nulos / no vacíos).
 * - Considera "discreta" si:
 *    - tiene más de 1 valor distinto
 *    - y los distintos <= min(20, max(2, floor(total*0.30)))
 * - Luego saca TOP valores (máx 10) con GROUP BY para dibujar tarta.
 */

function is_suspect_id_col(string $col): bool {
  $c = strtolower($col);
  if ($c === "id") return true;
  if (str_ends_with($c, "_id")) return true;
  if ($c === "created_at" || $c === "updated_at") return true;
  if ($c === "fecha" || str_contains($c, "fecha_")) return true; // sueles querer fechas como series, no como tarta
  return false;
}

function table_total_rows(string $tabla): int {
  $pdo = db();
  $st = $pdo->query("SELECT COUNT(*) AS n FROM $tabla");
  $r = $st->fetch();
  return (int)($r["n"] ?? 0);
}

function distinct_count(string $tabla, string $col): int {
  $pdo = db();
  $sql = "SELECT COUNT(DISTINCT NULLIF(TRIM(CAST($col AS TEXT)), '')) AS d
          FROM $tabla";
  $st = $pdo->query($sql);
  $r = $st->fetch();
  return (int)($r["d"] ?? 0);
}

function top_values(string $tabla, string $col, int $limit = 10): array {
  $pdo = db();
  $sql = "
    SELECT
      COALESCE(NULLIF(TRIM(CAST($col AS TEXT)), ''), '(vacío)') AS etiqueta,
      COUNT(*) AS valor
    FROM $tabla
    GROUP BY etiqueta
    ORDER BY valor DESC
    LIMIT " . (int)$limit;
  $st = $pdo->query($sql);
  return $st->fetchAll();
}

function pick_discrete_columns(string $tabla): array {
  $cols = table_columns($tabla);
  $total = table_total_rows($tabla);
  if ($total <= 0) return [];

  $maxDistinct = min(20, max(2, (int)floor($total * 0.30)));

  $discretas = [];
  foreach ($cols as $c) {
    $name = (string)$c["name"];
    $type = strtoupper((string)$c["type"]);
    $isPk = ((int)$c["pk"] === 1);

    if ($isPk) continue;
    if (is_suspect_id_col($name)) continue;

    // Evita columnas claramente continuas: precio, total, subtotal, etc.
    $lname = strtolower($name);
    if (preg_match('/(precio|total|subtotal|iva|importe|cantidad|saldo|coste|porcentaje|%)/i', $lname)) {
      continue;
    }

    // Si es numeric, solo lo aceptamos si realmente tiene pocos distintos (discreto)
    // Si es TEXT, también lo filtramos por distintos.
    $d = distinct_count($tabla, $name);

    if ($d > 1 && $d <= $maxDistinct) {
      $discretas[] = [
        "name" => $name,
        "type" => $type,
        "distinct" => $d,
        "total" => $total,
      ];
    }
  }

  // Orden: primero las más “útiles” (menos distintos, más compactas)
  usort($discretas, function($a,$b){
    return ($a["distinct"] <=> $b["distinct"]);
  });

  return $discretas;
}

// ==============================
// Render UI
// ==============================
$modulo = $_GET["modulo"] ?? "";
if (!isset($entidades) || !is_array($entidades)) {
  echo "<p>No hay entidades definidas para el módulo.</p>";
  return;
}

?>
<style>
/* Dashboard de gráficas (auto-contenido) */
.gdash{
  display:flex;
  flex-direction:column;
  gap:18px;
  max-width:1200px;
}
.gdash h2{ margin:0; }
.gbox{
  background:var(--card);
  border:1px solid var(--border);
  border-radius:var(--radius);
  box-shadow:var(--shadow);
  padding:16px;
}
.gentity{
  display:flex;
  flex-direction:column;
  gap:12px;
}
.ggrid{
  display:grid;
  grid-template-columns:repeat(auto-fit,minmax(320px,1fr));
  gap:14px;
}
.gcard{
  border:1px solid var(--border);
  border-radius:14px;
  padding:14px;
  display:flex;
  gap:14px;
  align-items:flex-start;
  background:#fff;
}
.gpie{
  width:160px;
  aspect-ratio:1;
  border-radius:50%;
  background:#eee;
  flex:0 0 auto;
  position:relative;
  border:1px solid rgba(0,0,0,.06);
}
.glegend{
  display:flex;
  flex-direction:column;
  gap:8px;
  min-width:140px;
}
.gtitle{
  font-weight:650;
  margin:0 0 4px 0;
}
.gmeta{
  font-size:12px;
  color:var(--muted);
  margin:0 0 8px 0;
}
.gli{
  display:flex;
  align-items:center;
  justify-content:space-between;
  gap:10px;
  font-size:13px;
  border-bottom:1px dashed rgba(0,0,0,.08);
  padding-bottom:6px;
}
.gli:last-child{ border-bottom:none; padding-bottom:0; }
.gdot{
  width:10px;height:10px;border-radius:999px;flex:0 0 auto;
}
.gleft{
  display:flex;align-items:center;gap:8px;min-width:0;
}
.gname{
  white-space:nowrap;
  overflow:hidden;
  text-overflow:ellipsis;
  max-width:210px;
}
.gval{
  font-variant-numeric: tabular-nums;
  color:var(--muted);
}
.gempty{
  color:var(--muted);
  font-size:13px;
}
</style>

<div class="gdash">
  <div class="gbox">
    <h2>Dashboard: <?= h(ucfirst($modulo)) ?></h2>
    <p class="gmeta" style="margin:6px 0 0 0;">
      Gráficas generadas automáticamente (solo columnas discretas / repetibles).
    </p>
  </div>

  <?php foreach($entidades as $tabla): ?>
    <?php
      $total = table_total_rows($tabla);
      $cols  = $total > 0 ? pick_discrete_columns($tabla) : [];
    ?>
    <div class="gbox gentity">
      <div style="display:flex;align-items:baseline;justify-content:space-between;gap:12px;">
        <h3 style="margin:0;">Entidad: <?= h($tabla) ?></h3>
        <span class="gmeta">Filas: <?= (int)$total ?></span>
      </div>

      <?php if($total <= 0): ?>
        <p class="gempty">No hay datos en esta entidad.</p>
      <?php elseif(!$cols): ?>
        <p class="gempty">No se han detectado columnas discretas/repetibles (según la heurística actual).</p>
      <?php else: ?>
        <div class="ggrid">
          <?php foreach($cols as $c): ?>
            <?php
              $col = $c["name"];
              $data = top_values($tabla, $col, 10);

              // si sale todo vacío o solo 1 etiqueta, no dibujamos
              if (!$data || count($data) < 2) continue;

              $payload = [
                "tabla" => $tabla,
                "col" => $col,
                "total" => $c["total"],
                "distinct" => $c["distinct"],
                "items" => array_map(function($r){
                  return [
                    "Etiqueta" => (string)$r["etiqueta"],
                    "Valor" => (int)$r["valor"],
                  ];
                }, $data),
              ];
            ?>
            <div class="gcard">
              <div class="gpie"
                   data-pie='<?= h(json_encode($payload, JSON_UNESCAPED_UNICODE)) ?>'></div>
              <div class="glegend">
                <p class="gtitle"><?= h($col) ?></p>
                <p class="gmeta">Distintos: <?= (int)$c["distinct"] ?> · Total: <?= (int)$c["total"] ?></p>
                <div class="gitems"></div>
              </div>
            </div>
          <?php endforeach; ?>
        </div>
      <?php endif; ?>
    </div>
  <?php endforeach; ?>
</div>

<script>
(function(){
  const PALETTE = [
    "#2f2e8b", "#ff6a00", "#4f46e5", "#06b6d4", "#10b981",
    "#f59e0b", "#ef4444", "#8b5cf6", "#22c55e", "#0ea5e9",
    "#f97316", "#14b8a6", "#e11d48", "#a855f7"
  ];

  function sum(arr){ return arr.reduce((a,b)=>a+b,0); }

  function buildGradient(items){
    const total = sum(items.map(x => x.Valor));
    let acc = 0;
    const parts = [];
    items.forEach((it, i) => {
      const start = acc / total * 100;
      acc += it.Valor;
      const end = acc / total * 100;
      const color = PALETTE[i % PALETTE.length];
      parts.push(`${color} ${start.toFixed(2)}% ${end.toFixed(2)}%`);
    });
    return `conic-gradient(${parts.join(",")})`;
  }

  function renderLegend(container, items){
    container.innerHTML = "";
    const total = sum(items.map(x => x.Valor));
    items.forEach((it, i) => {
      const color = PALETTE[i % PALETTE.length];
      const row = document.createElement("div");
      row.className = "gli";

      const left = document.createElement("div");
      left.className = "gleft";

      const dot = document.createElement("span");
      dot.className = "gdot";
      dot.style.background = color;

      const name = document.createElement("span");
      name.className = "gname";
      name.textContent = it.Etiqueta;

      left.appendChild(dot);
      left.appendChild(name);

      const val = document.createElement("span");
      val.className = "gval";
      const pct = total ? (it.Valor / total * 100) : 0;
      val.textContent = `${it.Valor} (${pct.toFixed(0)}%)`;

      row.appendChild(left);
      row.appendChild(val);

      container.appendChild(row);
    });
  }

  document.querySelectorAll(".gpie[data-pie]").forEach(pie => {
    let payload = null;
    try { payload = JSON.parse(pie.getAttribute("data-pie")); } catch(e){}

    if(!payload || !payload.items || payload.items.length < 2){
      pie.style.background = "#eee";
      return;
    }

    pie.style.background = buildGradient(payload.items);

    const legend = pie.parentElement.querySelector(".gitems");
    if(legend) renderLegend(legend, payload.items);
  });
})();
</script>