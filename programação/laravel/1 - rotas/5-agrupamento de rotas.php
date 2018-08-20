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

/*criação do grupo de rotas 'app'
o link dessas rotas sera 
site/gruporota/rota
ex:
localhost/app/pagina-cadastro
*/

Route::prefix('app')->group(function(){
    Route::get("/", function(){
        return "pagina principal";
    });

    Route::get("cadastro", function(){
        return "pagina-cadastro";
    });
});