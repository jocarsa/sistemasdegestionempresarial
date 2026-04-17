<?php

	/*
  	Archivo de login
    Contiene una conexión a la base de datos en PHP
    Y un formulario en HTML con usuario y contraseña
  */
  
	if(isset($_POST['usuario'])){
  	$db = new PDO('sqlite:db/empresa.db');		// Abro la base de datos
    $result = $db->query("
    	SELECT * FROM usuarios
      WHERE
      usuario = '".$_POST['usuario']."'
      AND
      contrasena = '".$_POST['contrasena']."'
      ");																				// Le pregunto a la base de datos si existe ese usuario
    if ($row = $result->fetch(PDO::FETCH_ASSOC)) {
      echo "pasas";															// Si existe pasas
      $_SESSION['usuario'] = $row['usuario'];
      header('Location: ?');
    }else{
    	echo "no pasas";													// Si no existe no pasas
    }
 	}
?>

<div class="centered-screen">

<form class="login-card" action="?" method="POST">

    <img src="static/logo.png" alt="Logo">

    <input
        type="text"
        name="usuario"
        placeholder="Usuario"
        required
    >

    <input
        type="password"
        name="contrasena"
        placeholder="Contraseña"
        required
    >

    <input type="submit" value="Entrar">

</form>

</div>