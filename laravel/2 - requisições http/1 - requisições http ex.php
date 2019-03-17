<?php
//REQUISICAO POST
route::post('/requisicao-page', function(){
    return "Hello(POST)";
});

//REQUISICAO GET
route::get('/requisicao-page', function(){
    return "Hello(GET)";
});

//REQUISICAO PUT
route::put('/requisicao-page', function(){
    return "Hello(PUT)";
});

//REQUISICAO OPTIONS
route::options('/requisicao-page', function(){
    return "Hello(OPTIONS)";
});

//REQUISICAO PATH
route::options('/requisicao-path', function(){
    return "Hello(PATH)";
});

/*
requisição: interação com determinado recurso 
recurso: alvo da requisição

GET
Solicita a representação de um determinado recurso. É definido como um método seguro e não deve ser usado para disparar uma ação (remover um usuário, por exemplo).
POST
As informações enviadas no corpo (body) da requisição são utilizadas para criar um novo recurso. Também é responsável por fazer processamentos que não são diretamente relacionados a um recurso.
DELETE
Remove um recurso. Deve retornar o status 204 caso não exista nenhum recurso para a URI especificada.
PUT
Atualiza um recurso na URI especificada. Caso o recurso não exista, ele pode criar um. A principal diferenteça entre POST e PUT é que o primeiro pode lidar não somente com recursos, mas pode fazer processamento de informações, por exemplo.
HEAD
Retorna informações sobre um recurso. Na prática, funciona semelhante ao método GET, mas sem retornar o recurso no corpo da requisição. Também é considerado um método seguro.
Os outros métodos disponíveis são OPTIONS, TRACE e CONNECT. Em teoria, os servidores devem implementar os métodos GET e HEAD e, sempre que possível, o método OPTIONS.

Status
Toda requisição recebe um código de resposta conhecido como status. Com o status é possível saber se uma operação foi realizada com sucesso (200), se ele foi movida e agora existe em outro lugar (301) ou se não existe mais (404).

Existem muitos status divididos em diversas categorias. Na especificação você pode ver cada um deles com uma descrição bastante detalhada. Abaixo, mostro alguns códigos que são mais frequentes.

200 OK
A requisição foi bem sucedida.
301 Moved Permanently
O recurso foi movido permanentemente para outra URI.
302 Found
O recurso foi movido temporariamente para outra URI.
304 Not Modified
O recurso não foi alterado.
401 Unauthorized
A URI especificada exige autenticação do cliente. O cliente pode tentar fazer novas requisições.
403 Forbidden
O servidor entende a requisição, mas se recusa em atendê-la. O cliente não deve tentar fazer uma nova requisição.
404 Not Found
O servidor não encontrou nenhuma URI correspondente.
405 Method Not Allowed
O método especificado na requisição não é válido na URI. A resposta deve incluir um cabeçalho Allow com uma lista dos métodos aceitos.
410 Gone
O recurso solicitado está indisponível mas seu endereço atual não é conhecido.
500 Internal Server Error
O servidor não foi capaz de concluir a requisição devido a um erro inesperado.
502 Bad Gateway
O servidor, enquanto agindo como proxy ou gateway, recebeu uma resposta inválida do servidor upstream a que fez uma requisição.
503 Service Unavailable
O servidor não é capaz de processar a requisição pois está temporariamente indisponível.

*/