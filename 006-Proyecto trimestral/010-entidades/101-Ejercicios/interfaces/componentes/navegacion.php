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