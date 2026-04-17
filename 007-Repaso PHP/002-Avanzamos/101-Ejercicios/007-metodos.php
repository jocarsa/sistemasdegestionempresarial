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
  $gato1->color = "naranja";
  echo $gato1->maulla();
  echo $gato1->color;
?>