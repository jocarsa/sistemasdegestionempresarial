<?php

class Gato {

    public $color;
    public $edad;

    function __construct(){
        $this->edad = 0;
        $this->color = "";
    }

    function maulla(){
        return "miau";
    }

    function setEdad($nuevaedad){
        if($this->edad == $nuevaedad - 1){
            $this->edad = $nuevaedad;
        }else{
            return "error";
        }
    }

    function getEdad(){
        return $this->edad;
    }
}

$gato1 = new Gato();

$gato1->setEdad(1);
echo "El gato tiene ".$gato1->getEdad()." años<br>";

$gato1->setEdad(5);   // error lógico
echo "El gato tiene ".$gato1->getEdad()." años";

?>