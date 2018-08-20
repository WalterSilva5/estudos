<?php
class documento{
    public $nome;
    protected $idade;
    private $senha;

    public function verDados(){
        echo $this->nome;
        echo "<br>";
        echo $this->idade;
        echo "<br>";
        echo $this->senha;
        echo "<br>";

    }
}

/*como o metodo verDados() é publico ele pode acessar
 * todos os dados dentro do objeto e mostralos fora
 *
 *public - visivel em todos os lugares
 *
 * protected - visivel apenas nas classes e nao nas instancias
 *
 * private - visivel apenas na classe pai
 */
?>