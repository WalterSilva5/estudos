<?php
$imagem = "imagens".DIRECTORY_SEPARATOR."imagem.png";
$content = file_get_contents($imagem);
$parse = parse_url($imagem);

$basename = basename($parse["path"]);

$file = fopen($basename, "w+");
fwrite($file, $content);
fclose($file);
?>

<img src="<?=$basename?>"/>