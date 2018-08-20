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
    if(!(isset($n))){
        echo "voce não passou um numero no parametro";
    }else if (!(is_integer($n))){
        echo "o parametro n não é um numero";
    }else{
        for($i=0; $i<$n;$i++){
            echo "$nome ($i)";
        }
    }
});