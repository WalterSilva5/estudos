<!DOCTYPE html>
<html lang = "pt-br">
<head>
	<meta charset="utf-8">
	<link rel="stylesheet" type="text/css" href="stylesheet.css">
		<title>Testes</title>
</head>
<body>
	<form method="POST">
		<input type="text" name="login"/>
		<br>
		<input type="password" name="senha">
		<input type="submit"/>
	</form>

	<?php
		$login = "walter";
		$senha = "1234";

		if ($_POST["login"]==$login && $_POST["senha"]==$senha){
			echo "Logado";
		}
		else{
			echo "Login ou Senha Incorreto";
		}
	?>

</body>
</html>