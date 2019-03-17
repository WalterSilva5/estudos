<?php
parar isso temos que criar uma rota 
para executar o metodo no controlador
que retorna a view

então no arquivo routes/web.php criamos a rota

Route::get('/produtos', 'produtoControlador@listar');

e na pasta resources/views criamos a view produtos.blade.php

e com o artisan criamos o controlador

php artisan make:controller produtoControlador

no controlador criamos o metodo listar

por exemplo:
    
public function listar(){
    $produtos = ["notebook", "televisão", "geladeira", "radio"];
    return view('produtos', ['computador'=>$produtos[0], 'refrigerador'=>$produtos[1]]);
}

ou:
public function listar(){
    $produtos = ["notebook", "televisão", "geladeira", "radio"];
    return view('produtos', $produtos);
}

essa view produtos é a view que esta na pasta projeto/resources/view/produtos.blade.php

//atenção
o array produtos é passado para a view ao executar o metodo 
se algo for passado para uma view
essa cois afica disponivel para ser acessado dentro da view

então se esta view recebeu um array ou uma variavel 

podemos pegar o conteudo dessa variavel dentro da view


