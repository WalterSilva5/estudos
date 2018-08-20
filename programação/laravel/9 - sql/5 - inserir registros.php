<?php
Route::get('/categorias', function(){
    DB::table('categorias')->insert(
        ['nome'=>'cimento']);
});


inserir com try:
try{
    DB::table('categorias')->insert(
        ['nome'=>'tenys']);
}catch(Exception $e){
    echo "Ocorreu um erro ao inserir, o campo ja existe</br>";
}