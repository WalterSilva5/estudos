<?php
//comando para rota
//arquivo routes/web.php
//metodo

Route::resource('/cliente', 'controladorCliente');


Route::resource('rota', 'classeControlador');

/*essa rota resource cria varias rotas para todos os metodos que estão
na classe controladorCliente

cada metodo é acessivel via uma rota diferente
os parametros tambem estão acessiveis*/


//metodo create
//metodo de requisição get | head
rota: /cliente/create
metodo: controladorCliente@create
//cria um novo cliente por exemplo


//metodo show 
//metodo de requisição get | head 
rota: /cliente/{cliente} 
metodo: controladorCliente@show
//retorna os detalhes de um cliente passado no parametro

//metodo update 
//metodo de requisição put | patch 
rota: /cliente/{cliente}
metodo: controladorCliente@update
//atualiza informações de um recurso

//metodo destroy
//metodo de requisição delete
rota: /cliente/{cliente}
metodo: controladorCliente@destroy
//apaga um cliente da base de dados

//metodo edit
//metodo de requisição get | head
rota: /cliente/{cliente}/edit
metodo: controladorCliente@edit
//mostra um formulario com as informações atuais do sistema
//esse formulario serve para editar/ atualizar as informações do cliente
