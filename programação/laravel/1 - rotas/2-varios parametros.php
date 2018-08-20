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

/*
*exemplo com varios parametros para a rota
*os parametros são os elementos dentro das chaves
*parametros dentro da função anonima são passados de forma posicionais
*não importa o nome dentro das chaves na rota oq importa são as posições 
*dentro do parametro da função anonima
*/
Route::get('/ola/{nome}', function ($nome) {
    return "<h1>ola ${nome} seja bem vindo</h1>";
});

//exemplo com um parametro
Route::get('/ola/{nome}'/*{nome} é o parametro da url*/, function ($nome/*parametro da função anonima*/) {
    return "<h1>ola ${nome} seja bem vindo</h1>";//parametro da função anonima no retorno
});

//exemplo com varios parametros
Route::get('/ola/{nome}/{sobrenome}', function ($nome,$sobrenome) {
    return "<h1>ola ${nome} ${sobrenome} seja bem vindo</h1>";
});

//o nome dos parametros não importa
Route::get('/ola/{nome}/{sobrenome}', function ($a,$b) {
    return "<h1>ola ${a} ${b} seja bem vindo</h1>";
});
//link dessa rota http://localhost/projeto/public/ola
