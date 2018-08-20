<!DOCTYPE html>
<html lang = "pt-br">
<head>
	<meta charset="utf-8">
	<link rel="stylesheet" type="text/css" href="stylesheet.css">
	<title>Testes</title>
</head>
<body>

	<?php
		echo $_POST["valor1"];
	?>

	<form method="POST">
		<input type="text" name="valor1"/>
		<input type="submit" />
	</form>

</body>
</html>