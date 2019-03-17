<?php

comando para criar um model atraves do artisan:
php artisan make:model nome_do_modelo

ex:
php artisan make:model categoria

se no banco de dados existir uma tabela com o nome categorias 
(com s no final)
    
esse model vai fazer referencia a essa tabela 
//////////////
o model categoria faz referencia a tabela categorias

para criar o model e a migration com um so comando basta usar 

php artisan make:model categoria -m 
    
o -m significa que queremos que seja criado o migration junto com o model
    

os models são criados na pasta app/