<?php
usar clausula like do sql 
$nomes = DB::table('categorias')->where('nome', 'like', 'c%')->pluck('nome');
foreach($nomes as $nome){
    echo "$nome </br>";
}
o 'like' é um parametro do where
'c%' quer dizer que queremos oq começar com a letra c

'nome' é a coluna que queremos recuperar os registros

///orWhere//////////////////
orWhere serve para encadear varios where

$nomes = DB::table('categorias')->where('id',1)->orWhere('id',2)->pluck('nome');
foreach($nomes as $nome){
    echo "$nome </br>";
}

///////whereBetween////////
whereBetween serve para recuperar os registros em um determinado intervalo
ex:
$nomes = DB::table('categorias')->whereBetween('id',[1,2])->pluck('nome');
foreach($nomes as $nome){
    echo "$nome </br>";
}
//nesse caso ele vai recuperar os ids no intervalo de 1 a 2
se fosse ('id', [0,5])
ele iria recuperar os elementos cujos ids esivessem de 0 ate 4
//inverso: whereNotbetween


//////////////////////whereIn///////////////////////
recuperar varios elementos com um so where:
$nomes = DB::table('categorias')->whereIn('id',[1,2])->pluck('nome');
foreach($nomes as $nome){
    echo "$nome </br>";
}

nesse caso ele ira retornar os elementos cujos ids sejam 1 ou 2
//inverso: whereNotIn
//////////////////////////////////////////////////////

encadeando varias comparações com um unico whereBetween
///para fazer isso precisamos passar um array de comparações

$nomes = DB::table('categorias')->where(
    [
        ['id', 1],
        ['nome', 'tvs'],
    ]
)->pluck('nome');
foreach($nomes as $nome){
    echo "$nome </br>";
}
