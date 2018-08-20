<?php

//no arquivo web.php
Route::get("/ola", function(){
    return view('ola');
});

//na pasta projeto/resources/view
//criamos um arquivo.blaze.php com a view ola

//ex dentro da view ola

<h1> ola mundo </h1>

//ao acessar a url ola o vamos pra view ola


//abreviação da rota 
Route::view('ola', 'ola');
//param1 url param2 nome da view