<?php
// interfaces/componentes/tabla.php
// Requiere: $tabla (array filas), $pk, $baseUrl

?>
<style>
  table{
    background:white;
    padding:20px;
    border-radius:10px;
    border-spacing:0;
    width:100%;
    max-width:1100px;
  }
  thead th{
    background:var(--corporativo);
    color:white;
    position:sticky;
    top:0;
  }
  thead th:first-child{ border-radius:12px 0 0 12px; }
  thead th:last-child{ border-radius:0 12px 12px 0; }
  th,td{ padding:10px; border-bottom:1px solid #eee; text-align:left; font-size:14px; }
  .acciones{ display:flex; gap:8px; }
  .a{
    border:1px solid #ddd;
    padding:6px 10px;
    border-radius:10px;
    text-decoration:none;
    color:inherit;
    font-size:13px;
    background:#fff;
  }
  .danger{
    border-color:#f1c0c0;
  }
  form{ margin:0; }
  button.bdel{
    border:1px solid #f1c0c0;
    background:white;
    padding:6px 10px;
    border-radius:10px;
    cursor:pointer;
    font-size:13px;
  }
</style>

<?php if(!$tabla || count($tabla) === 0): ?>
  <p>No hay registros.</p>
<?php else: ?>
<table>
  <thead>
    <tr>
      <?php foreach(array_keys($tabla[0]) as $k): ?>
        <th><?= h($k) ?></th>
      <?php endforeach; ?>
      <th>acciones</th>
    </tr>
  </thead>
  <tbody>
    <?php foreach($tabla as $fila): ?>
      <tr>
        <?php foreach($fila as $v): ?>
          <td><?= h($v) ?></td>
        <?php endforeach; ?>

        <td>
          <div class="acciones">
            <a class="a" href="<?= h($baseUrl . "&accion=edit&id=" . urlencode($fila[$pk])) ?>">Editar</a>

            <form method="POST" action="<?= h($baseUrl) ?>">
              <input type="hidden" name="__accion" value="delete">
              <input type="hidden" name="__id" value="<?= h($fila[$pk]) ?>">
              <button class="bdel" type="submit">Borrar</button>
            </form>
          </div>
        </td>
      </tr>
    <?php endforeach; ?>
  </tbody>
</table>
<?php endif; ?>