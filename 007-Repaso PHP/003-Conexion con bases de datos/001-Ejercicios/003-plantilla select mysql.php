<?php

  $conexion = new mysqli(
    "localhost",
    "pruebamysqlphp",
    "Pruebamysqlphp123$",
    "pruebamysqlphp"
  );

  $resultado = $conexion->query("
      SELECT * FROM clientes;
  ");
	
  while($fila = $resultado->fetch_array()){
  	var_dump($fila);
  }
  $conexion->close();

?>