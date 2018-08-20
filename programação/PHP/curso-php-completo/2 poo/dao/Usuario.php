<?php
require_once("config.php");
class Usuario{
    private $nome;
    private $idade;

    public function getNome(){
        return $this->nome;
    }
    private  function setNome($nomeDB){
        $this->nome = $nomeDB;
    }

    public function getIdade(){
        return $this->idade;
    }
    private  function setIdade($idadeDB){
        $this->idade = $idadeDB;
    }


    public function loadById($id){
        $sql = new Sql();
        $results = $sql->select("SELECT * FROM usuarios WHERE id = :ID", array(":ID"=>$id));

        if (count($results)>0){
            $row = $results[0];
            $this->setIdade($row["idade"]);
            $this->setNome($row["nome"]);
        }
    }

    public function mostrar(){
        $nome = $this->getNome();
        $idade = $this->getIdade();
        return "Nome: $nome, Idade: $idade";
    }
}

?>