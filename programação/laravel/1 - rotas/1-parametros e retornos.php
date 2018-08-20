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

/* Exemplo de rotas do laravel
o parametro antes da função anonima é a rota do sistema
a função anonima retorna uma view do php 
 */

Route::get('/'/*rota*/, function () {
    return view('welcome');/* rota retorna isso*/
});

Route::get('/ola', function () {
    return "<h1>seja bem vindo</h1>";
});

//link dessa rota http://localhost/projeto/public/ola
