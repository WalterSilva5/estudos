<?php

/*
na pasta padrão do projeto
roda o comando npm i
vai instalar as dependencias do npm 

as dependencias estão definidas no arquivo 
package.json
*/
##########################################
/* apos instalado temos que ir ate o arquivo
projeto/resoureces/assets/js/app.js

e no arquivo app.js
temos que comentar as linhas que contem referencia a vue

deixa so o requiere botstrap

/*

###########################################

/*
na pasta do projeto roda o comando npm run dev
isso vai compilar o js e o css que precisamos
para executar no projeto
*/

/*para testar cria uma pagina na pasta de views
no arquivo dessa pagina temos que incluir
o arquivo css e js 
que ficam na pasta public/css e public/js


ATENÇÂO: estes arquivos contem tudo necessario
ex: o do js ja tem o jquery e o vuejs dentro dele
o css ja tem o bootrapcss e outros codigos css dentro dele
*/

a linha de link desse arquivo no head sera 
<link href="{{asset('css/app.css')}}" rel="stylesheet">

e no body linkamos o outro arquivo
<script src="{{asset('js/app.js')}}" rel="text/javascript"></script>

//ATENÇÃO estas linhas devem estar no arquivo da view
#################################################

