<?php

/*
para que o laravel execute uma requisição de atualização
o formulario que vai atualizar os dados
tem que ter um parametro de tipo de requisição
e a requisição deve ser do tipo PUT

se verificarmos os metodos disponiveis
para as rotas do controlador
com o comando
php artisan route:list

vemos que metodo da requisição UPDATE deve ser do tipo
put

então para definir isso no formulario html
podemos colocar um campo adicional com o tipo da requisição

ATENÇÃO: enviamos o formulario como metodo POST
porem o formulario tem um campo oculto 

o tipo desse campo deve ser _method
o value desse campo deve ser PUT

esse campo deve ser oculto no formulario!!!

ex:
<input type="_method" value="PUT" style="display: none;"> 
*/