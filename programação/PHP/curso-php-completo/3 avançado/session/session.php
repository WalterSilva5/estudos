<?php
    session_start();

    //atribuir campos a session
    $_SESSION["nome"]="walter";
    $_SESSION["senha"]="1234";

    //encerrar sessao
    session_unset();//destroy a sessao
    //session_unset("nome")  //apaga apenas um campo da sessao
    //session_destroy() //destroy a sessao

    $id = session_id()//retorna o id da sessao
?>