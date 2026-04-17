<?php
// interfaces/componentes/formulario.php
declare(strict_types=1);

require_once __DIR__ . "/../../util/helpers.php";
require_once __DIR__ . "/../../util/crud.php";
require_once __DIR__ . "/../../util/schema_comments.php";

/**
 * Expected variables from caller (your base/crud_ui.php already does this):
 * - $tabla_nombre (string)
 * - $accion ('create'|'update')
 * - $valores (array) values (and for update: $valores['__id'])
 */

$tabla = (string)($tabla_nombre ?? "");
if ($tabla === "") {
  echo "<p>Formulario: tabla no indicada.</p>";
  return;
}

$accion = (string)($accion ?? "create");
if (!in_array($accion, ["create","update"], true)) $accion = "create";

$valores = is_array($valores ?? null) ? $valores : [];

$cols = table_columns($tabla);
$pk   = table_pk($tabla);

$tableComment = schema_table_comment($tabla);
$colComments  = schema_columns_comments($tabla);

function input_type_from_sqlite(string $type, string $name): string {
  $t = strtoupper($type);
  if (preg_match('/(DATE|TIME)/', $t) || preg_match('/(^fecha|date|datetime)/i', $name)) return "date";
  if (preg_match('/(INT)/', $t)) return "number";
  if (preg_match('/(REAL|FLOA|DOUB|DEC)/', $t)) return "number";
  if (preg_match('/(BOOL)/', $t)) return "number";
  if (preg_match('/(TEXT|CHAR|CLOB)/', $t)) return "text";
  return "text";
}
?>
<style>
  .form-wrap{
    background:#fff;
    border:1px solid rgba(0,0,0,.08);
    border-radius:14px;
    padding:14px;
    box-shadow: var(--shadow);
  }
  .form-wrap h3{
    margin:0 0 6px 0;
  }
  .form-desc{
    font-size:13px;
    opacity:.75;
    margin:0 0 14px 0;
    line-height:1.35;
  }
  .form-grid{
    
    gap:12px 14px;
  }
  .field{
    display:flex;
    flex-direction:column;
    gap:6px;
  }
  .field label{
    font-size:13px;
    font-weight:600;
    opacity:.9;
  }
  .field input, .field textarea, .field select{
    padding:10px 10px;
    border-radius:12px;
    border:1px solid rgba(0,0,0,.12);
    background:#fff;
    outline:none;
    font-size:14px;
  }
  .field textarea{
    min-height:90px;
    resize:vertical;
  }
  .help{
    font-size:12px;
    opacity:.70;
    line-height:1.25;
  }
  .actions{
    margin-top:14px;
    display:flex;
    gap:10px;
    align-items:center;
  }
  .actions button{
    padding:10px 14px;
    border-radius:12px;
    border:1px solid rgba(0,0,0,.12);
    background: rgba(0,0,0,.06);
    cursor:pointer;
    font-size:14px;
  }
  .actions a{
    text-decoration:none;
    opacity:.8;
  }
</style>

<div class="form-wrap">
  <h3><?= h($accion === "create" ? "Nuevo registro" : "Editar registro") ?> · <?= h($tabla) ?></h3>
  <?php if ($tableComment !== ""): ?>
    <p class="form-desc"><?= h($tableComment) ?></p>
  <?php endif; ?>

  <form method="post">
    <input type="hidden" name="__accion" value="<?= h($accion) ?>">
    <?php if ($accion === "update"): ?>
      <input type="hidden" name="__id" value="<?= h((string)($valores["__id"] ?? "")) ?>">
    <?php endif; ?>

    <div class="form-grid">
      <?php foreach ($cols as $c): ?>
        <?php
          $name = (string)$c["name"];
          $type = (string)($c["type"] ?? "");
          $isPk = (int)($c["pk"] ?? 0) === 1;

          if ($isPk) continue; // never edit PK

          $value = array_key_exists($name, $valores) ? (string)$valores[$name] : "";
          $comment = (string)($colComments[$name] ?? "");
          $inputType = input_type_from_sqlite($type, $name);

          // crude heuristic: long text fields -> textarea
          $useTextarea = (stripos($type, "TEXT") !== false) && (strlen($value) > 80 || preg_match('/(descripcion|observa|nota|coment)/i', $name));
        ?>
        <div class="field">
          <label for="<?= h($name) ?>" <?= $comment !== "" ? 'title="'.h($comment).'"' : '' ?>>
            <?= h($name) ?>
          </label>

          <?php if ($useTextarea): ?>
            <textarea id="<?= h($name) ?>" name="<?= h($name) ?>"><?= h($value) ?></textarea>
          <?php else: ?>
            <?php
              $step = (strpos(strtoupper($type), "REAL") !== false || strpos(strtoupper($type), "DEC") !== false) ? "0.01" : "1";
              $stepAttr = ($inputType === "number") ? ' step="'.h($step).'"' : '';
            ?>
            <input
              id="<?= h($name) ?>"
              name="<?= h($name) ?>"
              type="<?= h($inputType) ?>"
              value="<?= h($value) ?>"
              <?= $stepAttr ?>
            >
          <?php endif; ?>

          <?php if ($comment !== ""): ?>
            <div class="help"><?= h($comment) ?></div>
          <?php endif; ?>
        </div>
      <?php endforeach; ?>
    </div>

    <div class="actions">
      <button type="submit"><?= h($accion === "create" ? "Crear" : "Guardar") ?></button>
      <a href="javascript:history.back()">Cancelar</a>
    </div>
  </form>
</div>
