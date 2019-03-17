<?php
//no arquivo de controller
public function listar(){
    $produtos = ["notebook", "televisão", "geladeira", "radio"];
    return view('contar', compact('produtos',$produtos));
}

os parametros passados para a view 
devem ser um ARRAY ASSOCIATIVO !!! 
para q esse nesse caso o array produtos fique disponivel 
no arquivo de view passamos a função compact
para colocar o $produtos dentro de um array e com a chave 'produtos'

mas poderiamos ter tambem o caso 
public function listar(){
    $produtos = ['pc'=>"notebook",'tv'=>"televisão",'gl'=>"geladeira", 'som'=>"radio"];
    return view('produtos', $produtos);
}



nesse caso serão criadas variaveis com as chaves do array
como no caso a chave pc guarda o conteudo notebook
então na view ficara disponivel uma variavel $pc e seu conteudo sera 'notebook'
