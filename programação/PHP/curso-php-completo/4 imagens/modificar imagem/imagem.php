<?php

$image = imagecreatefromjpeg("certificado.jpg");
$tileColor = imagecolorallocate($image, 0, 0, 0);
$gray = imagecolorallocate($image, 100, 100, 100);

imagestring($image, 5, 450, 150, "certificaado", $tileColor);
imagestring($image, 5, 440, 350, "nome", $tileColor);
imagestring($image, 3, 440, 370, "data", $tileColor);

header("Content-type: image/jpeg");
imagejpeg($image, "imagem".date("d").".".jpg);
imagedestroy($image);
