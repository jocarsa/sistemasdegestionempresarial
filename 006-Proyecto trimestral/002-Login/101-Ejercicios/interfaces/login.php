<?php
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
    }else{
    	echo "no pasas";													// Si no existe no pasas
    }
 	}
?>
<style>
	body{display:flex;justify-content:center;align-items:center;}
  form{background:white;padding:20px;width:250px;height:400px;
  display:flex;flex-direction:column;gap:10px;justify-content:center;border-radius:5px;}
  input{padding:10px;border:1px solid var(--corporativo);outline:none;border-radius:5px;}
  input[type="submit"]{background:var(--corporativo);color:white;}
</style>
<form action="?" method="POST">
	<img src="static/logo.png" alt="Logo">
	<input 
  	type="text" 
    name="usuario" 
    placeholder="usuario"
  >
  <input 
  	type="password" 
    name="contrasena" 
    placeholder="contraseña"
  >
  <input type="submit">
</form>