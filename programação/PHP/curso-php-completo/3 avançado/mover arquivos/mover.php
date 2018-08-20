<?php
    $dir1 = "folder1";
    $dir2 = "folder2";

    if (!is_dir($dir1)) mkdir($dir1);
    if (!is_dir($dir2)) mkdir($dir2);

    $filename = "readme.txt";

    if(!file_exists($dir1.DIRECTORY_SEPARATOR.$filename)){
        $file = fopen($dir1.DIRECTORY_SEPARATOR.$filename, "w+");
        fwrite($file, date("Y-m-d H:i:s"));
        fclose($file);
    }

    rename(
        $dir1.DIRECTORY_SEPARATOR.$filename,
        $dir2.DIRECTORY_SEPARATOR.$filename
        );

    echo "Arquivo Movido!";
?>