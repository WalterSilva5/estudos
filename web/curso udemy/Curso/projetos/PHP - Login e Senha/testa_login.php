<?php
    $login = "walter";
    $senha = "1234";

    if ($_POST["login"] == $login AND $_POST["senha"]==$senha){
        echo "Login E Senha Corretos";
    }else{
        echo"Login Incorreto";
    }
?>