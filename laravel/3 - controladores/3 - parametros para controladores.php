<?php

//rota com parametros:
//arquivo routes/web.php
Route::get('/multiplicar/{n1}/{n2}', 'meuControlador@multiplicar');

//controlador
//arquivo App/Http/Controllers/meuControlador.php

namespace App\Http\Controllers;

use Illuminate\Http\Request;

class meuControlador extends Controller
{

    public function getNumero(){
        echo "Ola 1";
    }

    public function multiplicar($n1, $n2){
        return $n1*$n2;
    }
}


//na rota nao precisa passar os parametros no metodo
//apenas na rota mesmo do link