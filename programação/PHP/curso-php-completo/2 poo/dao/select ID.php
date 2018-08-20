<?php
    require_once("config.php");
    $nome = new Usuario();
    $nome->loadById(3);
    echo $nome->mostrar();
?>