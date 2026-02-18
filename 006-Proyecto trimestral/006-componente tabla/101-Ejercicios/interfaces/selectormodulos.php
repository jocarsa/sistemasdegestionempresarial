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

<div class="grid">
  <article>
  	<a href="?modulo=clientes">
      <img src="">
      <h3>Clientes</h3>
    </a>
  </article>
  <article>
  	<a href="?modulo=clientes">
      <img src="?modulo=clientes">
      <h3>Productos</h3>
    </a>
  </article>
  
</div>
