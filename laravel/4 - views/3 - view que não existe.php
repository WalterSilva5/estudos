<?php

//temos que testar se a view existe 
//usando o metodo estatico (View::exists('nome da view'))

//ex

Route::get('usuario/{nome}', function(){
    if (View::exists('usuario')){
        return view('usuario', compact('nome'));
    }
    else{
        return (view('erro'));
    }
    //essa view erro pode contar uma mensagem de erro
}); 