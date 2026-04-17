<?php
require_once __DIR__ . "/../util/helpers.php";
// base/crud_ui.php
require_once __DIR__ . "/../util/crud.php";

$modulo = $_GET["modulo"] ?? "";
$vista  = $_GET["vista"] ?? ($entidades[0] ?? "");
if (!in_array($vista, $entidades, true)) {
  echo "<p>Entidad no permitida.</p>";
  return;
}

$baseUrl = "?modulo=" . urlencode((string)$modulo) . "&vista=" . urlencode((string)$vista);

// Columns + PK
$cols = table_columns($vista);
$pk   = table_pk($vista);

// Detect date field (for calendar mode)
$dateField = "";
foreach ($cols as $c) {
  $name = (string)($c["name"] ?? "");
  $type = strtoupper((string)($c["type"] ?? ""));
  if ($name === "") continue;

  if (strpos($type, "DATE") !== false || strpos($type, "TIME") !== false) {
    $dateField = $name;
    break;
  }
}
if ($dateField === "") {
  foreach ($cols as $c) {
    $name = (string)($c["name"] ?? "");
    if ($name === "") continue;
    if (preg_match('/(^fecha|fecha$|_fecha_|date|datetime)/i', $name)) {
      $dateField = $name;
      break;
    }
  }
}

// Mode (table | cards | calendar)
$mode = (string)($_GET["mode"] ?? "table");
if (!in_array($mode, ["table","cards","calendar"], true)) $mode = "table";
if ($mode === "calendar" && $dateField === "") $mode = "table";

function build_url_with_mode(string $baseUrl, string $mode): string {
  $q = $_GET;
  $q["mode"] = $mode;
  // baseUrl already contains modulo+vista, but we build from $_GET for safety
  return "?" . http_build_query($q);
}

/*
  Acciones:
  - GET  accion=new | edit&id=...
  - POST __accion=create|update|delete
*/
if ($_SERVER["REQUEST_METHOD"] === "POST" && isset($_POST["__accion"])) {
  $accion = (string)$_POST["__accion"];

  // recoger datos (solo columnas reales no-PK)
  $permitidas = [];
  foreach ($cols as $c) if (!(int)$c["pk"]) $permitidas[] = (string)$c["name"];

  $data = [];
  foreach ($permitidas as $c) {
    if (array_key_exists($c, $_POST)) $data[$c] = $_POST[$c];
  }

  if ($accion === "create") {
    insert_row($vista, $data);
    header("Location: $baseUrl");
    exit;
  }

  if ($accion === "update") {
    $id = $_POST["__id"] ?? null;
    if ($id !== null) update_row($vista, $id, $data);
    header("Location: $baseUrl");
    exit;
  }

  if ($accion === "delete") {
    $id = $_POST["__id"] ?? null;
    if ($id !== null) delete_row($vista, $id);
    header("Location: $baseUrl");
    exit;
  }
}

// UI wrapper
echo '<div style="display:flex;flex-direction:column;gap:14px;">';

// Title
echo "<h2 style='margin:0;'>Entidad: " . h($vista) . "</h2>";

// Create button
$texto = "Crear nuevo";
$url   = $baseUrl . "&accion=new";
include __DIR__ . "/../interfaces/componentes/boton.php";

// NEW form
if (isset($_GET["accion"]) && $_GET["accion"] === "new") {
  $tabla_nombre = $vista;
  $accion = "create";
  $valores = [];
  include __DIR__ . "/../interfaces/componentes/formulario.php";
  echo "</div>";
  return;
}

// EDIT form
if (isset($_GET["accion"]) && $_GET["accion"] === "edit") {
  $id = $_GET["id"] ?? null;
  $row = $id ? get_row($vista, $id) : null;
  if (!$row) {
    echo "<p>No existe el registro.</p>";
    echo "</div>";
    return;
  }
  $tabla_nombre = $vista;
  $accion = "update";
  $valores = $row;
  $valores["__id"] = $row[$pk];
  include __DIR__ . "/../interfaces/componentes/formulario.php";
  echo "</div>";
  return;
}

/* =========================================================
   LISTING TOOLBAR (TABLE / CARDS / CALENDAR)
========================================================= */
?>
<style>
  .crud-toolbar{
    display:flex;
    align-items:center;
    justify-content:space-between;
    gap:12px;
    padding:10px 12px;
    border:1px solid rgba(0,0,0,.08);
    border-radius:12px;
    background:#fff;
    box-shadow: var(--shadow);
    margin: 0 0 6px 0;
  }
  .crud-toolbar .left{
    display:flex;
    align-items:center;
    gap:10px;
    min-width:0;
  }
  .crud-toolbar .title{
    font-weight:600;
    white-space:nowrap;
    overflow:hidden;
    text-overflow:ellipsis;
  }
  .crud-toolbar .right{
    display:flex;
    align-items:center;
    gap:8px;
  }
  .view-toggle{
    display:flex;
    gap:8px;
    flex-wrap:wrap;
    justify-content:flex-end;
  }
  .view-toggle a{
    text-decoration:none;
    color:inherit;
    padding:8px 10px;
    border-radius:10px;
    border:1px solid rgba(0,0,0,.10);
    background: rgba(0,0,0,.03);
    font-size:13px;
    display:inline-flex;
    align-items:center;
    gap:8px;
  }
  .view-toggle a.active{
    background: rgba(0,0,0,.10);
    border-color: rgba(0,0,0,.18);
  }
  .badge{
    font-size:12px;
    opacity:.65;
    padding:4px 8px;
    border-radius:999px;
    background: rgba(0,0,0,.05);
    border:1px solid rgba(0,0,0,.06);
    white-space:nowrap;
  }

  /* Cards view */
  .cards-grid{
    display:grid;
    grid-template-columns: repeat(auto-fill, minmax(260px, 1fr));
    gap:14px;
  }
  .card{
    background:#fff;
    border:1px solid rgba(0,0,0,.08);
    border-radius:14px;
    padding:14px;
    box-shadow: var(--shadow);
  }
  .card .head{
    display:flex;
    justify-content:space-between;
    align-items:center;
    gap:10px;
    margin-bottom:10px;
  }
  .card .id{
    font-weight:600;
    opacity:.85;
  }
  .card .actions{
    display:flex;
    gap:10px;
    font-size:13px;
    opacity:.85;
  }
  .card .actions a{
    text-decoration:none;
    color:inherit;
  }
  .kv{
    display:grid;
    grid-template-columns: 1fr;
    gap:6px;
    font-size:13px;
  }
  .kv .row{
    display:flex;
    gap:8px;
    min-width:0;
  }
  .kv .k{
    opacity:.6;
    width:120px;
    flex:0 0 auto;
  }
  .kv .v{
    min-width:0;
    overflow:hidden;
    text-overflow:ellipsis;
    white-space:nowrap;
  }

  /* Calendar view */
  .cal-wrap{
    background:#fff;
    border:1px solid rgba(0,0,0,.08);
    border-radius:14px;
    box-shadow: var(--shadow);
    padding:14px;
  }
  .cal-head{
    display:flex;
    justify-content:space-between;
    align-items:center;
    gap:10px;
    margin-bottom:12px;
  }
  .cal-grid{
    display:grid;
    grid-template-columns: repeat(7, 1fr);
    gap:8px;
  }
  .cal-dow{
    font-size:12px;
    opacity:.65;
    padding:6px 8px;
  }
  .cal-day{
    border:1px solid rgba(0,0,0,.08);
    border-radius:12px;
    min-height:74px;
    padding:8px;
    display:flex;
    flex-direction:column;
    gap:6px;
    background: rgba(0,0,0,.02);
  }
  .cal-day .n{
    font-size:12px;
    opacity:.75;
  }
  .cal-day .cnt{
    margin-top:auto;
    font-size:12px;
    padding:4px 8px;
    border-radius:999px;
    display:inline-block;
    width:fit-content;
    background: rgba(0,0,0,.08);
  }
  .cal-day.muted{
    opacity:.45;
  }
</style>

<div class="crud-toolbar">
  <div class="left">
    <div class="title">Listado</div>
    <?php if($dateField !== ""): ?>
      <div class="badge">📅 <?= h($dateField) ?></div>
    <?php endif; ?>
  </div>

  <div class="right">
    <div class="view-toggle" id="viewToggle">
      <a href="<?= h(build_url_with_mode($baseUrl, "table")) ?>"
         data-mode="table" class="<?= $mode==="table" ? "active" : "" ?>">📋 Tabla</a>

      <a href="<?= h(build_url_with_mode($baseUrl, "cards")) ?>"
         data-mode="cards" class="<?= $mode==="cards" ? "active" : "" ?>">🗂️ Tarjetas</a>

      <?php if($dateField !== ""): ?>
        <a href="<?= h(build_url_with_mode($baseUrl, "calendar")) ?>"
           data-mode="calendar" class="<?= $mode==="calendar" ? "active" : "" ?>">🗓️ Calendario</a>
      <?php endif; ?>
    </div>
  </div>
</div>

<script>
(function(){
  const key = "crud.mode.<?= addslashes($vista) ?>";
  document.querySelectorAll("#viewToggle a[data-mode]").forEach(a=>{
    a.addEventListener("click", ()=>{
      try{ localStorage.setItem(key, a.dataset.mode); }catch(e){}
    });
  });
})();
</script>
<?php

// listado data (we reuse your list_rows)
$tabla = list_rows($vista);

/* =========================================================
   RENDER: TABLE | CARDS | CALENDAR
========================================================= */

// TABLE (existing)
if ($mode === "table") {
  include __DIR__ . "/../interfaces/componentes/tabla.php";
  echo "</div>";
  return;
}

// CARDS
if ($mode === "cards") {
  if (!$tabla) {
    echo "<p>No hay registros.</p>";
    echo "</div>";
    return;
  }

  echo '<div class="cards-grid">';
  foreach ($tabla as $r) {
    $idVal = $r[$pk] ?? "";

    // choose up to 6 fields to show (excluding PK)
    $show = [];
    foreach ($cols as $c) {
      $name = (string)$c["name"];
      if ($name === $pk) continue;
      if (!array_key_exists($name, $r)) continue;

      $val = $r[$name];
      if ($val === null || $val === "") continue;

      $s = (string)$val;
      if (mb_strlen($s) > 120) $s = mb_substr($s, 0, 120) . "…";
      $show[] = [$name, $s];

      if (count($show) >= 6) break;
    }

    $editUrl = $baseUrl . "&accion=edit&id=" . urlencode((string)$idVal);
    $delUrl  = $baseUrl . "&accion=delete&id=" . urlencode((string)$idVal);

    echo '<div class="card">';
    echo '  <div class="head">';
    echo '    <div class="id">#' . h((string)$idVal) . '</div>';
    echo '    <div class="actions">';
    echo '      <a href="'.h($editUrl).'">Editar</a>';
    echo '      <form method="post" style="margin:0;display:inline;" onsubmit="return confirm(\'¿Eliminar este registro?\')">';
    echo '        <input type="hidden" name="__accion" value="delete">';
    echo '        <input type="hidden" name="__id" value="'.h((string)$idVal).'">';
    echo '        <button type="submit" style="border:none;background:none;padding:0;margin:0;cursor:pointer;font:inherit;opacity:.9;">Eliminar</button>';
    echo '      </form>';
    echo '    </div>';
    echo '  </div>';

    echo '  <div class="kv">';
    if (!$show) {
      echo '    <div class="row"><div class="k">—</div><div class="v">Sin datos</div></div>';
    } else {
      foreach ($show as [$k,$v]) {
        echo '    <div class="row"><div class="k">'.h($k).'</div><div class="v">'.h($v).'</div></div>';
      }
    }
    echo '  </div>';
    echo '</div>';
  }
  echo '</div>';

  echo "</div>";
  return;
}

// CALENDAR (only if dateField exists; mode already forced back to table otherwise)
if ($mode === "calendar") {
  if (!$tabla) {
    echo "<p>No hay registros.</p>";
    echo "</div>";
    return;
  }

  // Month selection
  $month = (string)($_GET["month"] ?? date("Y-m"));
  if (!preg_match('/^\d{4}-\d{2}$/', $month)) $month = date("Y-m");

  // Counts per date (YYYY-MM-DD)
  $counts = [];
  foreach ($tabla as $r) {
    $raw = (string)($r[$dateField] ?? "");
    if ($raw === "") continue;
    $d = substr($raw, 0, 10);
    if (!preg_match('/^\d{4}-\d{2}-\d{2}$/', $d)) continue;
    $counts[$d] = ($counts[$d] ?? 0) + 1;
  }
  $countsJson = json_encode($counts, JSON_UNESCAPED_UNICODE|JSON_UNESCAPED_SLASHES);

  // Render calendar shell
  echo '<div class="cal-wrap">';
  echo '  <div class="cal-head">';
  echo '    <div style="font-weight:600;">Calendario · '.h($vista).'</div>';
  echo '    <form method="get" style="display:flex;gap:8px;align-items:center;margin:0;">';

  // keep params
  $keep = $_GET;
  unset($keep["month"]);
  foreach ($keep as $k=>$v) {
    echo '<input type="hidden" name="'.h((string)$k).'" value="'.h((string)$v).'">';
  }

  echo '      <input type="month" name="month" value="'.h($month).'">';
  echo '      <button type="submit">Ir</button>';
  echo '    </form>';
  echo '  </div>';
  echo '  <div class="cal-grid" id="calendarGrid"></div>';
  echo '</div>';

  ?>
  <script>
  (function(){
    const counts = <?= $countsJson ?: "{}" ?>;
    const month = "<?= addslashes($month) ?>"; // YYYY-MM
    const grid = document.getElementById("calendarGrid");

    const dows = ["L","M","X","J","V","S","D"]; // Monday-first
    dows.forEach(d=>{
      const el = document.createElement("div");
      el.className = "cal-dow";
      el.textContent = d;
      grid.appendChild(el);
    });

    const [Y,M] = month.split("-").map(Number);
    const first = new Date(Y, M-1, 1);
    const last  = new Date(Y, M, 0);

    const jsDow = first.getDay(); // 0=Sun
    const offset = (jsDow + 6) % 7; // Monday-first
    const daysInMonth = last.getDate();

    // previous month tail
    const prevLast = new Date(Y, M-1, 0).getDate();
    for(let i=0;i<offset;i++){
      const n = prevLast - offset + 1 + i;
      const cell = document.createElement("div");
      cell.className = "cal-day muted";
      cell.innerHTML = '<div class="n">'+n+'</div>';
      grid.appendChild(cell);
    }

    for(let day=1; day<=daysInMonth; day++){
      const d = String(day).padStart(2,"0");
      const key = `${Y}-${String(M).padStart(2,"0")}-${d}`;
      const cell = document.createElement("div");
      cell.className = "cal-day";

      const c = counts[key] || 0;
      cell.innerHTML = `
        <div class="n">${day}</div>
        ${c ? `<div class="cnt">${c} registros</div>` : `<div class="cnt" style="opacity:.45;">0</div>`}
      `;
      grid.appendChild(cell);
    }

    // fill to complete weeks (optional)
    const cellsUsed = offset + daysInMonth;
    const extra = (7 - (cellsUsed % 7)) % 7;
    for(let i=0;i<extra;i++){
      const cell = document.createElement("div");
      cell.className = "cal-day muted";
      cell.innerHTML = '<div class="n"></div>';
      grid.appendChild(cell);
    }
  })();
  </script>
  <?php

  echo "</div>";
  return;
}

// fallback
include __DIR__ . "/../interfaces/componentes/tabla.php";
echo "</div>";
