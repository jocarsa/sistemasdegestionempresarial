<?php
// interfaces/modulo.php
require_once __DIR__ . "/../util/helpers.php";
require_once __DIR__ . "/../util/modulos.php";

$slug = (string)($_GET["modulo"] ?? "");
if ($slug === "") {
  echo "<p>Módulo no indicado.</p>";
  return;
}

$modulo = modulos_obtener_por_slug($slug);
if (!$modulo || (int)$modulo["activo"] !== 1) {
  echo "<p>Módulo no válido.</p>";
  return;
}

$entidades = modulos_entidades_por_slug($slug);
if (!$entidades) {
  echo "<p>Este módulo no tiene entidades configuradas.</p>";
  return;
}

// Validación extra: la vista pedida debe estar en entidades del módulo
$vista = $_GET["vista"] ?? "";
if ($vista !== "" && !in_array($vista, $entidades, true)) {
  echo "<p>Entidad no permitida en este módulo.</p>";
  return;
}

// UI reutiliza tus componentes existentes
include __DIR__ . "/componentes/navegacion.php";
?>
<section>
  <?php
    if(!isset($_GET["vista"]) || $_GET["vista"] === ""){
      include __DIR__ . "/../base/graficas_ui.php";
    }else{
      include __DIR__ . "/../base/crud_ui.php";
    }
  ?>
</section>
