<?php

class Calculadora{
    
    private $numero1;
    private $numero2;
    private $total;
    
    function __construct(){
        $this->numero1 = 0;
        $this->numero2 = 0;
        $this->total = 0;
    }
    public function setNumero1($parametro_numero_1){
        $this->numero1 = $parametro_numero_1;
    }
    public function setNumero2($parametro_numero_2){
        $this->numero2 = $parametro_numero_2;
    }
    public function somar(){
        $this->total = $this->numero1 + $this->numero2;
    }
    public function subtrair(){
        $this->total = $this->numero1 - $this->numero2;
    }
    public function multiplicar(){
        $this->total = $this->numero1 * $this->numero2;
    }
    public function dividir(){
        $this->total = $this->numero1 / $this->numero2;
    }
    public function getTotal(){
        return $this->total; 
    }
}
?>