<?php

ex criado com o parametro --create na migration:
Schema::create('produtos', function (Blueprint $table) {
    $table->increments('id');
    $table->timestamps();
});

criar colunas na tabela
$table->string('nome');
$table->float('preco');
$table->integer('estoque');

ex de uso:
Schema::create('produtos', function (Blueprint $table) {
    $table->increments('id');
    $table->string('nome');
    $table->float('preco');
    $table->integer('estoque');
    $table->timestamps();
});

executar migração:
php artisan migrate

desfazer migração:
php artisan migrate:rollback

criar migration com parametro de criação de tabelas:
php artisan make:migration criar_tabela_categorias --create=criar_tabela_categorias
categorias sera o nome da tabela

colocar palavras com s no nome das tabelas