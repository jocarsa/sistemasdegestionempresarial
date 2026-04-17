<?php
	if(isset($_GET['usuario'])){
  	
    	$db = new PDO("sqlite:../db/empresa.db");

		$stmt = $db->query("

        SELECT 
          *
        FROM api_keys
        WHERE 
        usuario = '".$_GET['usuario']."'
        AND 
        contrasena = '".$_GET['contrasena']."'
        ");
        
			$data = $stmt->fetchAll(PDO::FETCH_ASSOC);
      
      if($data){
      	$stmt = $db->query("

        SELECT 
          nombre,
          descripcion,
          precio 
        FROM productos
        WHERE activo = 1");

      	$data = $stmt->fetchAll(PDO::FETCH_ASSOC);

      	echo json_encode($data);
      }else{
    	header("HTTP/1.1 401 Unauthorized");
			exit;
    }
  }else{
    	die("Parametros no correctos");
    }
	

?>