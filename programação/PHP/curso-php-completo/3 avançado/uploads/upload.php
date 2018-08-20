<form method="post" enctype="multipart/form-data">
    <input type="file" name="imagem">
    <br/>
    <input type="submit" value="Enviar">
</form>
<?php
    if($_SERVER["REQUEST_METHOD"]==="POST"){
        $file = $_FILES["imagem"];

        if($file["error"]){
            throw new Exception("ERROR".$file["error"]);
        }
    }

    $dirUploads = "uploads";
    if (!is_dir("$dirUploads")){
        mkdir($dirUploads);
    }

    if(move_uploaded_file($file["tmp_name"],$dirUploads.DIRECTORY_SEPARATOR.$file["name"])){
        echo "upload feito";
    }else{
        throw new Exception("Erro no upload");
    }

?>