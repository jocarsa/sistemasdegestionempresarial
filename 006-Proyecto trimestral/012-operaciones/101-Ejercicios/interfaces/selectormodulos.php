<?php
	/*
  	Selector de módulos
    Este archivo muestra los módulos que estarán disponibles
    Por el momento es un archivo estático
    🟨TODO: Convertirlo en dinámico
  */
?>
<style>
  body{
    margin:0;
    min-height:100vh;
    display:flex;
    justify-content:center;
    align-items:center;
    background:var(--corporativo);
  }

  .grid{
    display:grid;
    grid-template-columns:repeat(4, 1fr);
    gap:20px;
  }

  article{
    background:white;
    height:100px;
    padding:20px;
    text-align:center;
    display:flex;
    flex-direction:column;
    justify-content:center;
    align-items:center;
    border-radius:10px;
  }
</style>

<div class="modulos-wrapper">

<div class="grid">

  <article class="modulo-card">
    <a href="?modulo=ventas">
      <h3>Ventas</h3>
    </a>
  </article>

  <article class="modulo-card">
    <a href="?modulo=produccion">
      <h3>Producción</h3>
    </a>
  </article>

  <article class="modulo-card">
    <a href="?modulo=facturacion">
      <h3>Facturación</h3>
    </a>
  </article>

</div>

</div>
