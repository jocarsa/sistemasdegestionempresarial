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
  		$leyenda = $entidad;
      $destino = $entidad;
  		include "interfaces/componentes/boton.php"; 
    }
  ?>
  
</nav>