<style>
	nav{
  	display:flex;
  	flex:1;
    flex-direction:column;
    gap:20px;
    padding:20px;
  }
  nav a,nav a button{
  	width:100%;
    text-align:left;
  }
</style>
<nav>
<?php
foreach($entidades as $entidad){

    $texto = ucfirst($entidad);
    $url = "?modulo=" . urlencode($_GET["modulo"])
         . "&vista=" . urlencode($entidad);

    include "interfaces/componentes/boton.php";
}
?>
<hr style="opacity:.2;width:100%;">
<?php
$texto = "Volver";
    $url = "./";
    include "interfaces/componentes/boton.php"; 
?>

<hr style="opacity:.2;width:100%;">

<?php
$texto = "Salir";
$url   = "util/cerrarsesion.php";
include "interfaces/componentes/boton.php";
?>
 
  
</nav>
