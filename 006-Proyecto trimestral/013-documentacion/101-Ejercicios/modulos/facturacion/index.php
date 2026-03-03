<style> section{ flex:5; } </style>

<?php
$entidades = ['clientes','facturas','pedidos'];
include "interfaces/componentes/navegacion.php";
?>

<section>
  <?php include "base/crud_ui.php"; ?>
</section>