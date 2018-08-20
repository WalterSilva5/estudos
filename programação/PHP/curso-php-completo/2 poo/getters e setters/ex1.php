<?php


class pessoa{
    private $nome;
    private $idade;

    public function getIdade()
    {
        return $this->idade;
    }

    public function setIdade($idade)
    {
        $this->idade = $idade;
    }

    public function getNome(){
        return $this->nome;
    }

    public function setNome($nome){
        $this->nome = $nome;
    }

    public function exibir(){
        return array(
            "nome"=>$this->getNome(),
            "idade"=>$this->getIdade()
        );
    }
}

$usuario = new pessoa();
$usuario->setNome("walter");
$usuario->setIdade(21);

$nome = $usuario->getNome();
$idade = $usuario->getIdade();
echo "Nome: $nome, idade: $idade";