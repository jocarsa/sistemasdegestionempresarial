<?php
	$leyenda = "Crear nuevo cliente";
  $destino = "crearnuevocliente.php";
	include "interfaces/componentes/boton.php";
  $tabla = [];
  $db = new PDO('sqlite:db/empresa.db');		// Abro la base de datos
    $result = $db->query(" SELECT * FROM clientes ");																				// Le pregunto a la base de datos si existe ese usuario
    while ($row = $result->fetch(PDO::FETCH_ASSOC)) {
      $tabla[] = $row;
    }
  
  include "interfaces/componentes/tabla.php";
?>