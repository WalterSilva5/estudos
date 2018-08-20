<!DOCTYPE html>
<html lang = "pt-br">
<head>
	<meta charset="utf-8">
	<link rel="stylesheet" type="text/css" href="stylesheet.css">
	<title>Titulo</title>
</head>
<body>
	<?php
		$conta = 0;
		echo $conta."<br>";
		do{
			$conta = $conta+1;
		}while($conta <10);

		echo $conta;

	?>
</body>
</html>