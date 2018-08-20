<?php
class Usuario
{
    private $nome;
    private $idade;

    public function getNome()
    {
        return $this->nome;
    }
    public function setNome($nome)
    {
        $this->nome = $nome;
    }

    public function getIdade()
    {
        return $this->idade;
    }
    public function setIdade($idade)
    {
        $this->idade= $idade;
    }

    public function loadByID($id){
        $sql = new Sql();
        $results = $sql->select("SELECT * FROM usuarios WHERE id = :ID", array(
            ":ID"=>$id
        ));
        if (isset($results[0])){
            $row = $results[0];
            $this->setNome($row["nome"]);
            $this->setIdade($row["idade"]);
        }
    }

    public static function search($nome){
        $sql = new Sql();
        return $sql->select("SELECT * FROM usuarios WHERE nome LIKE :SEARCH ORDER BY nome", array(
            ":SEARCH"=>"%".$nome."%"
        ));

    }

    public static function getList(){
        $sql = new Sql();
        return $sql->select("SELECT * FROM usuarios ORDER BY nome");
    }

    public function __toString()
    {
        return json_encode(
            array(

            )
        );
    }

    public function login($nome, $senha){
        $sql = new Sql();
        $logar = $sql->select("SELECT * FROM usuarios WHERE nome=:NOME and senha=:SENHA", array(
            ":NOME"=>$nome,
            ":SENHA"=>$senha
        ));
        if(isset($logar[0])){
            echo "LOGADO";
        }else{
            echo "erro ao logar";
        }
    }

    public function update($nome, $idade, $id){
        $this->setNome($nome);
        $this->setIdade($idade);

        $sql = new Sql();
        $sql->query("UPDATE usuarios SET nome = :NOME, idade = :IDADE WHERE id = :ID", array(
           ':NOME'=>$this->getNome(),
           ':IDADE'=>$this->getIdade(),
            'ID'=>$id
        ));
    }

    public  function delete($id){
        $sql = new Sql();
        $sql->query("DELETE FROM usuarios WHERE id=:ID",array(
            "ID"=>$id
        ));
    }

}