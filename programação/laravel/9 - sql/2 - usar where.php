<?php

ex com select :
$retorno = DB::table('categorias')->where('id',1)->get();

exibir:
$retorno = DB::table('categorias')->where('id',1)->get();
foreach ($retorno as $r){
    echo $r->nome;
}

se formos recuperar apenas um registro podemos no lugar do parametro ->get();
usar o parametro ->first();

nesse caso não precisamos percorrer com foreach o  array pois o parametro 
recebido vai ser de apenas um elemento