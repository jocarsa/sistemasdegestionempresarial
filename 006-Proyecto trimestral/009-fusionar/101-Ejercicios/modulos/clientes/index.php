	<style>
  	section{
    	flex:5;
    }
  </style>
  <?php include "interfaces/componentes/navegacion.php"?>
    <section>
      <?php
        $leyenda = "Crear nuevo cliente";
        $destino = "?modulo=".$_GET['modulo']."&operacion=insertar";
        include "interfaces/componentes/boton.php";
        $tabla = [];
        $db = new PDO('sqlite:db/empresa.db');		// Abro la base de datos
          $result = $db->query(" SELECT * FROM clientes ");																				// Le pregunto a la base de datos si existe ese usuario
          while ($row = $result->fetch(PDO::FETCH_ASSOC)) {
            $tabla[] = $row;
          }
				if(isset($_GET['operacion'])){
        	if($_GET['operacion'] == "insertar"){
          	include "interfaces/componentes/formulario.php";
          }
        }else{
        	include "interfaces/componentes/tabla.php";
        }
      ?>
    </section>