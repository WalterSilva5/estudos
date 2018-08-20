<?php
require_once("calculadora.php");
$numero1 = $_POST['num1'];
$numero2 = $_POST['num2'];
$operacao = $_POST['operacao'];
$calculadora = new Calculadora();

$calculadora->setNumero1($numero1);
$calculadora->setNumero2($numero2);

if($operacao == 'somar'){
    $calculadora->somar();
}else if($operacao == 'subtrair'){
    $calculadora->subtrair();
}else if($operacao == 'multiplicar'){
    $calculadora->multiplicar();
}else if($operacao == 'dividir'){
    $calculadora->dividir();
}



echo $calculadora->getTotal();

?>