<?php
spl_autoload_register(function($nome_da_classe){
   $file_name = "classes".DIRECTORY_SEPARATOR.$nome_da_classe.".php";
    if(file_exists($file_name)){
        require_once($file_name);
    }
});