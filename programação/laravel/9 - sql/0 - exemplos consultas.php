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

use Illuminate\Support\Facades\DB;


Route::get('/', function () {
    return view('welcome');
});


Route::get('/categorias', function(){
    $retorno = DB::table('categorias')->get();
    foreach($retorno as $campo){
        echo "id: ".$campo->id." ; ";
        echo "nome: ".$campo->nome." ;</br>";
    }

    echo "</br>--------------------------------</br>";
    $nomes = DB::table('categorias')->pluck('nome');
    foreach($nomes as $nome){
        echo "$nome </br>";
    }
    echo "</br>--------------------------------</br>";
    $retorno = DB::table('categorias')->where('id',2)->get();
    foreach ($retorno as $r){
        echo $r->nome;
    }

    echo "</br>--------------------------------</br>";
    $nomes = DB::table('categorias')->where('nome', 'like', 'c%')->pluck('nome');
    foreach($nomes as $nome){
        echo "$nome </br>";
    }
    echo "</br>--------------------------------</br>";

    $nomes = DB::table('categorias')->where('id',1)->orWhere('id',2)->pluck('nome');
    echo "orWhere </br>";
    foreach($nomes as $nome){
        echo "$nome </br>";
    }

    echo "</br>--------------------------------</br>";
    echo "whereBetweeen </br>";
    $nomes = DB::table('categorias')->whereBetween('id',[0,3])->pluck('nome');
    foreach($nomes as $nome){
        echo "$nome </br>";
    }
    echo "</br>--------------------------------</br>";
    $nomes = DB::table('categorias')->whereIn('id',[1,2])->pluck('nome');
    foreach($nomes as $nome){
        echo "$nome </br>";
    }
    echo "</br>--------------------------------</br>";
    $nomes = DB::table('categorias')->where(
        [
            ['id', 1],
            ['nome', 'tvs'],
        ]
    )->pluck('nome');
    foreach($nomes as $nome){
        echo "$nome </br>";
    }
    echo "</br>--------------------------------</br>";
    $retorno = DB::table('categorias')->orderBy('nome')->get();
    foreach($retorno as $campo){
        echo "id: ".$campo->id." ; ";
        echo "nome: ".$campo->nome." ;</br>";
    }
    echo "</br>--------------------------------</br>";
        $retorno = DB::table('categorias')->orderBy('nome', 'desc')->get();
        foreach($retorno as $campo){
            echo "id: ".$campo->id." ; ";
            echo "nome: ".$campo->nome." ;</br>";
        }
});