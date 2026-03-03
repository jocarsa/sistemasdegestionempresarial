<?php
// interfaces/componentes/formulario.php
// Requiere: $tabla_nombre, $cols, $baseUrl, $accion ("create"|"update"), $valores (array)
if (!isset($valores)) $valores = [];
if (!isset($accion)) $accion = "create";


?>
<style>
  form.crud{
    display:flex;
    flex-direction:column;
    gap:10px;
    max-width:520px;
  }
  .fila{
    display:flex;
    flex-direction:column;
    gap:6px;
  }
  label{ font-size:13px; opacity:.85; }
  input,select,textarea{
    border:1px solid #ddd;
    padding:10px;
    border-radius:8px;
    outline:none;
    font-size:14px;
  }
  input:focus,textarea:focus{ border-color: var(--corporativo); }
  .acciones{
    display:flex; gap:10px; margin-top:10px;
  }
  .submit{
    background:var(--corporativo);
    color:white;
    border:none;
    padding:10px 14px;
    border-radius:10px;
    cursor:pointer;
  }
  .link{
    display:inline-flex;
    align-items:center;
    padding:10px 14px;
    border-radius:10px;
    border:1px solid #ddd;
    text-decoration:none;
    color:inherit;
  }
</style>

<form class="crud" method="POST" action="<?= h($baseUrl) ?>">
  <input type="hidden" name="__accion" value="<?= h($accion) ?>">
  <?php if(isset($valores["__id"])): ?>
    <input type="hidden" name="__id" value="<?= h($valores["__id"]) ?>">
  <?php endif; ?>

  <?php foreach($cols as $c):
    $name = $c["name"];
    if ($c["pk"]) continue; // no editar PK

    $tipo = strtoupper((string)$c["type"]);
    $value = $valores[$name] ?? "";
    $inputType = "text";
    if (str_contains($tipo, "INT")) $inputType = "number";
    if (str_contains($tipo, "REAL") || str_contains($tipo, "FLOA") || str_contains($tipo,"DOUB")) $inputType = "number";
    if ($name === "email") $inputType = "email";
  ?>
    <div class="fila">
      <label><?= h($name) ?></label>

      <?php if($inputType === "number"): ?>
        <input type="number" step="any" name="<?= h($name) ?>" value="<?= h($value) ?>">
      <?php else: ?>
        <input type="<?= h($inputType) ?>" name="<?= h($name) ?>" value="<?= h($value) ?>">
      <?php endif; ?>

    </div>
  <?php endforeach; ?>

  <div class="acciones">
    <button class="submit" type="submit">
      <?= $accion === "update" ? "Guardar cambios" : "Crear" ?>
    </button>
    <a class="link" href="<?= h($baseUrl) ?>">Cancelar</a>
  </div>
</form>