<?php
$data = array(
    "nome"=>"walter"
);

setcookie("nome_cookie", json_encode($data), time()+3600);

echo "criado";