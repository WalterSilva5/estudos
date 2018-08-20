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


Route::get("/", function(){
    return "pagina-/";
});

Route::get("/a", function(){
    return "pagina-a";
});
Route::get("/c", function(){
    return "pagina-c";
});


/*Redirecionamento de rota /c para a /a
*/
Route::redirect('/c', '/a', 301);
