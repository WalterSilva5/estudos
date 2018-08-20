<?php

$image = imagecreatefromjpeg("certificado.jpg");
$tileColor = imagecolorallocate($image, 0, 0, 0);
$gray = imagecolorallocate($image, 100, 100, 100);

imagettftext($image, 32, 0,320, 250,$tileColor,"fonts".DIRECTORY_SEPARATOR."Bevan.ttf", "Certificado");
imagettftext($image, 32, 0,375, 350,$tileColor,"fonts".DIRECTORY_SEPARATOR."Playball.ttf","Nome");
imagestring($image, 3, 440, 370, utf8_decode("Concluido em: ").date("d/m/Y"), $tileColor);

header("Content-type: image/jpeg");
imagejpeg($image, "imagem.jpg");
imagedestroy($image);