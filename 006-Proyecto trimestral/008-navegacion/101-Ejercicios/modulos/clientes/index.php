	<nav>
    	<?php
      	$leyenda = "boton1";
      	include "interfaces/componentes/boton.php";  
      ?>
      <?php
      	$leyenda = "boton2";
      	include "interfaces/componentes/boton.php";  
      ?>
      <?php
      	$leyenda = "boton3";
      	include "interfaces/componentes/boton.php";  
      ?>
    </nav>
    <main>
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
    </main>