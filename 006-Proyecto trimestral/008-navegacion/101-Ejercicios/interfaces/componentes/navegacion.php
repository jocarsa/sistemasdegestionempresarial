<style>
	nav{
  	flex:1;
    flex-direction:column;
    gap:20px;
    padding:20px;
  }
</style>
<nav>
  <?php
  	$leyenda = "boton1";
  	include "interfaces/componentes/boton.php";  
  ?>
  <?php
  	$leyenda = "boton2";
  	include "interfaces/componentes/boton.php";  
  ?>
  <?php
  	$leyenda = "boton3";
  	include "interfaces/componentes/boton.php";  
  ?>
</nav>