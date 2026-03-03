<?php
	session_start(); 
  require_once "util/helpers.php";   // ✅ AÑADIR ESTO
  include "util/saneador.php";
?>
<!doctype html>
<html lang="es">
	<head>
  	<title>SSGG</title>
    <meta charset="utf-8">
    <link rel="stylesheet" href="base/estilo/comun.css">
  </head>
  <body>
  	
    <main>
    <?php
    
    	// Router //////////////////////////////////////////////////////
      
    	if(!isset($_SESSION['usuario'])){					// Si no existe la variable de sesion usuario
      	include "interfaces/login.php";					// Carga el login para que pueda iniciar sesion
      }else{
      	if(isset($_GET['modulo'])){
  include "interfaces/modulo.php";
}else{
  include "interfaces/selectormodulos.php";
}
      }
    ?>
    </main>
  </body>
</html>
