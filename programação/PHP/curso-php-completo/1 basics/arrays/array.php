<?php
$pessoas = ["walter", "wanderson"];

foreach ($pessoas as $pessoa){
    echo $pessoa."<br>";
}

//adicionar elemento
echo "<br/> teste2 <br/> <br/>";
array_push($pessoas, "luciene");
foreach ($pessoas as $pessoa){
    echo $pessoa."<br>";
}

//remover elemento
echo "<br/> teste3 <br/> <br/>" ;
unset($pessoas[2]);
foreach ($pessoas as $pessoa){
    echo $pessoa."<br>";
}

