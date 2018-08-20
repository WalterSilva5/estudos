<!DOCTYPE htmml>

<html lang = "pt-br">
<head>
    <meta charset ="utf-8">
    <link type="text-css" rel="stylesheet" href="stylesheet.css">
    <title></title>
</head>
<body>
   <form method="POST">
        <input type="text" name="dependentes">
        <input type="submit">
    </form>
    
    <?php

    $conta = 0;
    if(isset($_POST["dependentes"])){
        $dependente = $_POST["dependentes"];
        if(!is_numeric($dependente)){
            $dependente = 1;
            echo "Digite um numero!";

        }
        echo "<table border='1'>
        <tr>
            <th></th>
            <th>Nome</th>
            <th>Nascimento</th>                
        </tr>";
        do{
            echo "<tr>
                <td>Dependente</td>
                <td><input type='text' name='nome'></td>
                <td><input type='text' name='nasc'></td>
            </tr>";

            $conta++;

        }while ($conta<$dependente);
        echo "</table>";        
    }
    ?>
</body>
</html>
