<?php
class Usuario{
    private $nome;

    public function __construct()
    {
        $this->nome = "walter";
        echo $this->nome;
    }
}

$usuario = new Usuario();//instanciamos a classe
?>