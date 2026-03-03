<?php
require_once __DIR__ . "/../util/helpers.php";
require_once __DIR__ . "/../util/modulos.php";

$modulos = modulos_listar_activos();
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
    grid-template-columns:repeat(auto-fit, minmax(180px, 1fr));
    gap:20px;
    width:min(900px, 92vw);
  }
  article{
    background:white;
    height:110px;
    padding:20px;
    text-align:center;
    display:flex;
    flex-direction:column;
    justify-content:center;
    align-items:center;
    border-radius:14px;
    box-shadow: var(--shadow);
    border:1px solid rgba(0,0,0,.06);
  }
  article a{
    text-decoration:none;
    color:inherit;
    width:100%;
    height:100%;
    display:flex;
    flex-direction:column;
    justify-content:center;
    gap:6px;
  }
  article:hover{
    transform: translateY(-2px);
    transition:.12s;
  }
</style>

<div class="modulos-wrapper">
  <div class="grid">
    <?php if(!$modulos): ?>
      <article><a href="#"><h3>No hay módulos</h3></a></article>
    <?php else: ?>
      <?php foreach($modulos as $m): ?>
        <article class="modulo-card">
          <a href="?modulo=<?= h($m["slug"]) ?>">
            <h3 style="margin:0;"><?= h($m["nombre"]) ?></h3>
            <div style="font-size:12px;opacity:.7;"><?= h($m["slug"]) ?></div>
          </a>
        </article>
      <?php endforeach; ?>
    <?php endif; ?>
  </div>
</div>
