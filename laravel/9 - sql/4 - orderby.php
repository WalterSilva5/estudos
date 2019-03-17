<?php
Route::get('/categorias', function(){
    $retorno = DB::table('categorias')->orderBy('nome')->get();
    foreach($retorno as $campo){
        echo "id: ".$campo->id." ; ";
        echo "nome: ".$campo->nome." ;</br>";
    }
});

o retorno sera ordenado pelos nomes do retorno

//inverter o orderby
echo "</br>--------------------------------</br>";
    
Route::get('/categorias', function(){
    $retorno = DB::table('categorias')->orderBy('nome', 'desc')->get();
    foreach($retorno as $campo){
        echo "id: ".$campo->id." ; ";
        echo "nome: ".$campo->nome." ;</br>";
    }
});

//basta adicionar o parametro 'desc' ao orderBy