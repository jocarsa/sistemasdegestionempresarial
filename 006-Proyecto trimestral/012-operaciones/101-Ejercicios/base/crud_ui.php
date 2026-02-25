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

$baseUrl = "?modulo=" . urlencode($modulo) . "&vista=" . urlencode($vista);

$cols = table_columns($vista);
$pk   = table_pk($vista);

/*
  Acciones:
  - GET  accion=new | edit&id=...
  - POST __accion=create|update|delete
*/
if ($_SERVER["REQUEST_METHOD"] === "POST" && isset($_POST["__accion"])) {
  $accion = $_POST["__accion"];

  // recoger datos (solo columnas reales no-PK)
  $permitidas = [];
  foreach ($cols as $c) if (!(int)$c["pk"]) $permitidas[] = $c["name"];

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

// UI
echo '<div style="display:flex;flex-direction:column;gap:14px;">';
echo "<h2 style='margin:0;'>Entidad: " . h($vista) . "</h2>";

$leyenda = "Crear nuevo";
$href = $baseUrl . "&accion=new";
include __DIR__ . "/../interfaces/componentes/boton.php";

if (isset($_GET["accion"]) && $_GET["accion"] === "new") {
  $tabla_nombre = $vista;
  $accion = "create";
  $valores = [];
  include __DIR__ . "/../interfaces/componentes/formulario.php";
  echo "</div>";
  return;
}

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

// listado
$tabla = list_rows($vista);
include __DIR__ . "/../interfaces/componentes/tabla.php";
echo "</div>";