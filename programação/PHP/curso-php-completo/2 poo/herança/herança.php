<?php
class Documento{
    private $numero;
    public function getNumero(){
        return $this->numero;
    }
    public function setNumero($numero){
        $this->numero = $numero;
    }
}

class CPF extends Documento{
    public function validar():string{
        if (strlen($this->getNumero()) == 3){
            return "valido";
        }
        else{
            return "invalido";
        }
    }
}

$doc = new CPF();
$doc->setNumero(1234);
echo $doc->validar();
