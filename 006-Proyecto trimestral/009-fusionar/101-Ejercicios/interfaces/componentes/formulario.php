<?php
	$formulario = [
    'nombre',
    'apellidos',
    'email',
    'direccion'
  ];
?>
<style>
	form{display:flex;flex-direction:column;gap:10px;}
  input{border:1px solid #ff4400;padding:10px;}
  input[type="submit"]{background:#ff4400;color:white;}
</style>
<form action="?" method="POST">
	<?php
  	foreach($formulario as $campo){
    	echo '<input 
      	type="text" 
        name="'.$campo.'" 
        placeholder="'.$campo.'"
      >';
    }
  ?>
  <input type="submit">
</form>