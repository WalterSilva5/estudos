<?
/*blade serve para manipularmos o template da view

por exemplo se a view receber como parametro um nome
podemos mostrar esse nome assim:
*/

//<h1>ola {{$nome}}</h1>

// essas chaves duplas no blade servem para mostrar um parametro recebido

//a rota no arquivo routes/web.php fica
Route::get('/ola', function(){
    return view('minhaView')->with('nome', 'walter');
});

//o campo ->with() 
//serve para passar os parametros para a view

//tambem pode passar assim por get

Route::get('/ola/{nome}', function($nome){
    return view('minhaView')->with('nome', $nome);
});

//pode tambem passar um array de parametros
//sem usar o with
Route::get('/ola/{nome}', function($nome){
    $parametros=['nome'=>$nome];
    return view('minhaView', $parametros);
});
