<?php
	/* 
  	Componente botón
    Este componente declara un boton y lo estiliza
    Primero cargamos el estilo
    Y luego creamos el marcaje del boton
  */

?>
<link rel="stylesheet" href="../../base/estilo/comun.css">
<style>
	button{
  	background:white;
    border:2px solid var(--corporativo);
    padding:5px 10px 5px 5px;
    border-radius:30px;
  }
  .inicial{
  	background:var(--corporativo);
    padding:10px;
    border-radius:20px;
    width:10px;
    height:10px;
    color:white;
    font-size:10px;
    display:inline-block;
  }
</style>
<a href="<?= $destino ?>">
	<button>
  	<span class="inicial"><?= $leyenda[0] ?></span>
  	<?= $leyenda ?>
  </button>
</a>