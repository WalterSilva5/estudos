<?php
o arquivo .env da pasta do projeto
guarda as informações sobre o projeto

algumas coisas terão que ser modificadas nesse arquivo

a linha APP_NAME = laravel
guarda o nome da aplicação

APP_URL = localhost
guarda o link de acesso da aplicação

parte do db:

DB_CONNECTION=nome do banco

DB_HOST = url onde o banco se encontra

DB_PORT = porta de acesso ao db

DB_DATABASE = nome da database que queremos usar
DB_USERNAME = login do banco
DB_PASSWORD = senha do banco 

//////////////////ex////////////////////
//////////////////ex////////////////////

APP_NAME=Laravel
APP_ENV=local
APP_KEY=base64:LX0aO1LSXxOtcyxdif6Mm3LBg3TaBYN4I+dD9laoC5o=
APP_DEBUG=true
APP_URL=http://localhost

LOG_CHANNEL=stack

DB_CONNECTION=mysql
DB_HOST=127.0.0.1
DB_PORT=3306
DB_DATABASE=vendas
DB_USERNAME=root
DB_PASSWORD=

BROADCAST_DRIVER=log
CACHE_DRIVER=file
SESSION_DRIVER=file
SESSION_LIFETIME=120
QUEUE_DRIVER=sync

REDIS_HOST=127.0.0.1
REDIS_PASSWORD=null
REDIS_PORT=6379

MAIL_DRIVER=smtp
MAIL_HOST=smtp.mailtrap.io
MAIL_PORT=2525
MAIL_USERNAME=null
MAIL_PASSWORD=null
MAIL_ENCRYPTION=null

PUSHER_APP_ID=
PUSHER_APP_KEY=
PUSHER_APP_SECRET=
PUSHER_APP_CLUSTER=mt1

MIX_PUSHER_APP_KEY="${PUSHER_APP_KEY}"
MIX_PUSHER_APP_CLUSTER="${PUSHER_APP_CLUSTER}"

//////////////////ex////////////////////
//////////////////ex////////////////////
