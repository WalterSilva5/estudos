<?php

/*
|--------------------------------------------------------------------------
| Web Routes
|--------------------------------------------------------------------------
|
| Here is where you can register web routes for your application. These
| routes are loaded by the RouteServiceProvider within a group which
| contains the "web" middleware group. Now create something great!
|
*/


Route::get('/regras/{nome}/{n}', function ($nome, $n) {
    for($i=0;$i<$n;$i++){
        echo "ola $nome ($n)";
    }
})->where('n','[0-9]+');

/*where é a restrição do parametro
n é o parametro
'[0-9]+' é a expressão regular que siginifica que
a regra para n é ser de 0 a 9 ou então n tem que ser um numero 
*/

Route::get('/regras/{nome}/{n}', function ($nome, $n) {
    for($i=0;$i<$n;$i++){
        echo "ola $nome ($n)";
    }
})->where('n','[0-9]+')->where('nome','[a-z]+');

/*
'nome','[a-z]+' é a expressão regular de que nome tem que ser escrito
apenas com caracteres minusculos de a ate z 
*/