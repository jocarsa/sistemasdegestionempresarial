<?php
	class Gato{
  	function constructor(){
      $this->color;
      $this->edad;
    }
    
    function maulla(){
    	return "miau";
    }
    function setEdad($nuevaedad){
    	$this->edad = $nuevaedad;
    }
    function getEdad(){
    	return $this->edad;
    }
  }
  
  $gato1 = new Gato();
  $gato1->setEdad(0);
  echo "el gato tiene ".$gato1->getEdad()." años";
  $gato1->setEdad(5);
  echo "el gato tiene ".$gato1->getEdad()." años";
?>