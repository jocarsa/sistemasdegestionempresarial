<?php
	class Gato{
  	function constructor(){
      $this->color;
      $this->edad;
    }
    
    function maulla(){
    	return "miau";
    }
  }
  
  $gato1 = new Gato();
  $gato1->edad = 0;
  echo "el gato tiene ".$gato1->edad." años";
  $gato1->edad = 5;
  echo "el gato tiene ".$gato1->edad." años";
?>