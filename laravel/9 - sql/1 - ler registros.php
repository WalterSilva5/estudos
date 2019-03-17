<?php 
ler os registros do exemplo categorias

para poder usar os comandos sql no codigo devemos colocar essa linha
nas primeiras linhas do arquivo de rotas :

use Illuminate\Support\Facades\DB;

//////////////////////////////////////
rota para usar o comando sql:

Route::get('/categorias', function(){
    $retorno = DB::table('categorias')->get();
    foreach($retorno as $campo){
        echo "id: ".$campo->id." ; ";
        echo "nome: ".$campo->nome." ;</br>";
    }
});

insert into categorias(nome) values('televisao')

receber um array com os nomes das categorias;

$nomes =DB::table('categorias')->pluck('nome');
foreach($nomes as $nome){
    echo "$nome </br>";
}

//a função pluck serve para passarmos o campo no qual queremos para o array
