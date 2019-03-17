<?php

/*este arquivo que extende o 
arquivo app.blade.php da pasta leyout 
deve ficar na pasta views
e ele deve extender o app

por exemplo o arquivo filho.blade.php
o conteudo dele sera: */

@extends('layout.app')
@extends('pasta.template') 

/*o arquivo filho apenas extende o arquivo pai
então caso queira mostrar algo do filho no esqueleto do pai
devemos definir no pai onde este conteudo deve ser exibido
*/

//devemos criar uma sessao no filho por ex

@section('conteudo')
    <p> este conteudo esta no filho</p>
@endsection

//e no pai devemos definir onde esta sessao sera mostrada
//para definir isso usamos o metodo do blade yield()

@endsection// define a sessão e finaliza a definição

@show// mostra a sessão assim que finalizala

