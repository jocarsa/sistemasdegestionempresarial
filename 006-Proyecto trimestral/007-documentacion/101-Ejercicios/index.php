<?php
	session_start(); 
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
    <?php
    	if(!isset($_SESSION['usuario'])){					// Si no existe la variable de sesion usuario
      	include "interfaces/login.php";					// Carga el login para que pueda iniciar sesion
      }else{
      	if(isset($_GET['modulo'])){
        	include "modulos/".$_GET['modulo']."/index.php";
        }else{
        	include "interfaces/selectormodulos.php";	// Cargame el escritorio
        }
      }
    ?>
  </body>
</html>