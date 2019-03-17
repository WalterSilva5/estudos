<?php
//executar metodo do controlador a partir de rota

//criamos uma rota no arquivo routes/web.php

Route::get('/nome', "meuControlador@getnome");

//ou

Route::get('/rota',  "controlador@metodo");