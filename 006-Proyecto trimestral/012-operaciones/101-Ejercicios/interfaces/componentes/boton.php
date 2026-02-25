<?php
// interfaces/componentes/boton.php
if (!isset($leyenda)) $leyenda = "Botón";
if (!isset($href)) {
  // modo navegación a entidad
  $destino = $destino ?? ($leyenda ?? "");
  $href = "?modulo=" . urlencode($_GET["modulo"] ?? "") . "&vista=" . urlencode($destino);
}
?>
<link rel="stylesheet" href="base/estilo/comun.css">
<style>
  .btn{
    display:inline-flex;
    align-items:center;
    gap:10px;
    background:white;
    border:2px solid var(--corporativo);
    padding:8px 14px 8px 10px;
    border-radius:30px;
    cursor:pointer;
    text-decoration:none;
    color:inherit;
    font-size:14px;
  }
  .btn:hover{ filter:brightness(0.98); }
  .inicial{
    background:var(--corporativo);
    padding:8px;
    border-radius:16px;
    min-width:16px;
    height:16px;
    color:white;
    font-size:11px;
    display:inline-flex;
    align-items:center;
    justify-content:center;
    line-height:1;
  }
</style>

<a class="btn" href="<?= htmlspecialchars($href, ENT_QUOTES, 'UTF-8') ?>">
  <span class="inicial"><?= htmlspecialchars(mb_substr($leyenda,0,1), ENT_QUOTES, 'UTF-8') ?></span>
  <span><?= htmlspecialchars($leyenda, ENT_QUOTES, 'UTF-8') ?></span>
</a>