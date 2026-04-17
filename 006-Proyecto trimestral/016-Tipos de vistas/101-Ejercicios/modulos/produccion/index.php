<style> section{ flex:5; } </style>

<?php
$entidades = ['productos'];
include "interfaces/componentes/navegacion.php";
?>

<section>
  <?php
    if(!isset($_GET["vista"]) || $_GET["vista"] === ""){
      include "base/graficas_ui.php";
    }else{
      include "base/crud_ui.php";
    }
  ?>
</section>