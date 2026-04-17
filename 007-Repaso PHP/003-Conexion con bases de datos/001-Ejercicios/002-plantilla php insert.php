<?php

  $conexion = new mysqli(
    "localhost",
    "pruebamysqlphp",
    "Pruebamysqlphp123$",
    "pruebamysqlphp"
  );

  $conexion->query("
      INSERT INTO clientes
      VALUES (
        NULL,
        'Jose Vicente',
        'Carratala Sanchis',
        'juan@email.com',
        'La Calle de Jose Vicente'
      )
  ");

  $conexion->close();

?>