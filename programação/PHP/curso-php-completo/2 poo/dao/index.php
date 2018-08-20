<?php

require_once ("config.php");
/*carrega um usuario
 * $root = new Usuario;
 * $root->loadByID(3);
 * echo json_encode($root)
*/

/* carrega lista de todos os usuarios e ordena pelo login
 * require_once ("config.php");
 * $lista = Usuario::getList();
 * echo json_encode($lista);
*/

/*faz uma busca por um pdaço de texto
$search = Usuario::search("wa");
echo json_encode($search);
*/


/*carrega usuarios usando login e senha
$usuario = new Usuario();
$usuario->login("walter", 1234);
echo $usuario;
*/

/*atualizar campos da tabela
$usuario = new Usuario();
$usuario->loadByID(2);
$usuario->update("walter", 21, 2);
*/
/*deletar usuario por id
$usuario = new Usuario();
$usuario->delete(2);
*/