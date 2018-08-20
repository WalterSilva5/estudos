<?php

namespace App\Http\Controllers;

use Illuminate\Http\Request;

class contar extends Controller
{
    public function contar(){
        $numeros = ['n'=>1];
        return view('contar', $numeros);
    }
}
