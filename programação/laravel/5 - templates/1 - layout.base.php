<?php

/*na pasta views criamos uma pasta leyout
e dentro desta pasta criamos um arquivo 
para guardar o template base do site

por ex            */?>
<!DOCTYPE html>
<html lang="pt-br">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta http-equiv="X-UA-Compatible" content="ie=edge">
    <title></title>
</head>
<body>
    <div>
        //conteudo
    </div>
</body>
</html>

<?php
/* este esqueleto do site deve ficar 
escrito em um arquivo app.blade.php
*/


ex com css e javascript ja no codigo depois de instalar com npm i
    
<html>
<head>
    <link href="{{asset('css/app.css')}}" rel="stylesheet">
    //podemos criar um arquivo css na pasta public css
    <link href="{{asset('css/meuCss.css')}}" rel="stylesheet">
    <title>Inicio do site</title>
</head>
<body>
<div class="container bg-info">
    <h1>Inicio do site</h1>
</div>

<script src="{{asset('js/app.js')}}" rel="text/javascript"></script>
</body>
</html>