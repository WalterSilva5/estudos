<?php
/**
 * a interface define como uma classe deve se comportar
 * serve como base para que pessoas possam usar classes
 * criadas por outras pessoas
 */

interface Veiculo{
    public function acelerar($velocidade);
    public function trocarMarcha($marcha);
}

class Carro implements Veiculo{
    public function acelerar($velocidade){
        echo "chegou a velocidade $velocidade";
    }
    public function trocarMarcha($marcha){
        echo "mudou para a $marcha marcha";
    }
}

$fusca = new Carro();

$fusca->acelerar(10);
echo "<br>";
$fusca->trocarMarcha(10);