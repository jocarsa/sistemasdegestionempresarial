<?php
// boton.php
// REQUIRED:
//   $texto
//   $url

if(!isset($texto)) $texto = "Botón";
if(!isset($url))   $url   = "#";
?>

<a class="btn" href="<?= h($url) ?>">
    <span class="inicial">
        <?= h(mb_substr($texto,0,1)) ?>
    </span>
    <span><?= h($texto) ?></span>
</a>