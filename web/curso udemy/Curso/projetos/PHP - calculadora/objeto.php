
<?php
    class Pessoa{ 
        var $nome;

        function setNome($nome_definido){
            $this->nome = $nome_definido;
        }

        function getNome(){
            return $this->nome;
        }
    }

$pessoa = new Pessoa();
$pessoa->setNome("teste");
echo $pessoa->getNome();
?>