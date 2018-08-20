<?php
spl_autoload_register( function ($classe){
    $class_name = "classes".DIRECTORY_SEPARATOR.$classe.".php";
    if(file_exists($class_name)){
        require_once ($class_name);
    }
});