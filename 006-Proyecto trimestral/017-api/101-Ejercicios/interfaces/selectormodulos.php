<?php
// interfaces/selectormodulos.php
require_once __DIR__ . "/../util/helpers.php";
require_once __DIR__ . "/../util/modulos.php";

$modulos = modulos_listar_activos();
?>
<style>
  body{
    margin:0;
    min-height:100vh;
    background:var(--corporativo);
    font-family: system-ui, -apple-system, "Segoe UI", Roboto, Arial, sans-serif;
  }

  /* wrapper centers horizontally but keeps natural vertical flow */
  .modulos-wrapper{
    max-width:1200px;
    margin:0 auto;
    padding:60px 30px;
  }

  /* responsive grid */
  .grid{
    display:grid;
    grid-template-columns:repeat(auto-fill, minmax(260px, 1fr));
    gap:28px;
  }

  /* card */
  article{
    background:#fff;
    border-radius:16px;
    padding:22px;
    box-shadow: var(--shadow);
    border:1px solid rgba(0,0,0,.06);
    transition: transform .15s ease, box-shadow .15s ease;
  }

  article:hover{
    transform: translateY(-4px);
    box-shadow: 0 10px 30px rgba(0,0,0,.12);
  }

  article a{
    text-decoration:none;
    color:inherit;
    display:flex;
    align-items:center;
    gap:18px;
  }

  /* emoji */
  .emoji{
    font-size:38px;
    width:60px;
    height:60px;
    display:flex;
    align-items:center;
    justify-content:center;
    border-radius:14px;
    background:rgba(0,0,0,.05);
    flex-shrink:0;
  }

  /* text */
  .title{
    display:flex;
    flex-direction:column;
    gap:6px;
    min-width:0;
  }

  .title h3{
    margin:0;
    font-size:18px;
    font-weight:600;
    line-height:1.2;
    white-space:nowrap;
    overflow:hidden;
    text-overflow:ellipsis;
  }

  .title .slug{
    font-size:13px;
    opacity:.6;
    white-space:nowrap;
    overflow:hidden;
    text-overflow:ellipsis;
  }
</style>

<div class="modulos-wrapper">
  <div class="grid">
    <?php if(!$modulos): ?>
      <article>
        <a href="#">
          <div class="emoji">📦</div>
          <div class="title">
            <h3>No hay módulos</h3>
            <div class="slug">—</div>
          </div>
        </a>
      </article>
    <?php else: ?>
      <?php foreach($modulos as $m): ?>
        <?php
          $slug  = (string)($m["slug"] ?? "");
          $name  = (string)($m["nombre"] ?? $slug);
          $emoji = trim((string)($m["emoji"] ?? ""));
          if($emoji === "") $emoji = "📦";
        ?>
        <article>
          <a href="?modulo=<?= h($slug) ?>">
            <div class="emoji"><?= h($emoji) ?></div>
            <div class="title">
              <h3><?= h($name) ?></h3>
              <div class="slug"><?= h($slug) ?></div>
            </div>
          </a>
        </article>
      <?php endforeach; ?>
    <?php endif; ?>
  </div>
</div>
