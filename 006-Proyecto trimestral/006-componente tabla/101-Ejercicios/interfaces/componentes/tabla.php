<style>
	table{
    background:white;
    padding:20px;
    border-radius:10px;
    border-spacing: 0;
  }
  table thead tr th{
  	background:var(--corporativo);
    color:white;
    overflow:hidden;
  }
  table thead tr th:first-child{
  	border-radius:20px 0px 0px 20px;
  }
  table thead tr th:last-child{
  	border-radius:0px 20px 20px 0px;
  }
  table th,table td{padding:10px;border-collapse:collapse;}
</style>
<table>
	<thead>
  	<tr>
    	<?php
      	foreach($tabla[0] as $clave=>$valor){
        	echo '<th>'.$clave.'</th>';
        }
      ?>
    </tr>
  </thead>
  <tbody>
  	<?php
    		foreach($tabla as $fila){
        echo '<tr>';
          foreach($fila as $clave=>$valor){
            echo '<td>'.$valor.'</td>';
          }
        echo '</tr>';
        }
      ?>
  </tbody>
</table>