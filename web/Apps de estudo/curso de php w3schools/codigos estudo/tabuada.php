<!DOCTYPE htmml>

<html lang = "pt-br">
<head>
    <meta charset ="utf-8">
    <link type="text-css" rel="stylesheet" href="stylesheet.css">
    <title></title>
</head>
<body>
    <?php
        if(isset($_POST["tabuada"])){
            $tabuada =  $_POST["tabuada"];
                if($tabuada == "*"){
                    for($x=1;$x<=10;$x++){
                        for($y=1;$y<=10;$y++){
                            echo "(".$x."*".$y.")"."=".$x*$y."<br>";
                        };
                    echo "<br>";
                    };
                };
        };
    ?>

    <p>Digite o simbolo da tabuada que deseja ver</p>
    <form method="POST">
        <input type="text" name = "tabuada">
        <input type="submit">
    </form>


 
</body>
</html>
