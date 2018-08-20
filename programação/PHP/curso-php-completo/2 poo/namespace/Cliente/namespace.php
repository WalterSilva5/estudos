<?php

namespace Cliente;
/* cliente é o nome da pasta atual do
 * se eu importar algo que tem o mesmo nome
 * tenho que passar o caminho do arquivo no import
*/
class Cadastro extends \Cadastro{
    public $nome;
    public function getNome()
    {
        return $this->nome;
    }
    public function setNome(){
        $this->nome = $this->enviaNome();
    }
}

$nome = new Cadastro();
$nome->setNome();
$nome->getNome();