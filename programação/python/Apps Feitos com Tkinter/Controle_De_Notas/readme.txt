#Feito por Walter Stark

esse software é livre assim como seu codigo!

Uma professora que dava aulas de reforço em uma escola municipal estava tendo dificuldades
para organizar as notas dos alunos dela pois ela queria que os alunos tivessem niveis
de acordo com as suas presenças então elas valeriam pontos para a nota final do semestre
então ela me pediu para que eu fizesse algo para ajudala e eu desenvolvi esse software com 
o basico que sabia sobre python.

#Sobre os arquivos

'Cadastro Professor.pyw'
	é a janela de cadastro para o professor, o login e a senha digitados nela são salvos no arquivo professor.pck, com esse login e a senha é possivel logar no programa principal.
'professor.pck'
	é o arquivo que guarda o login e senha do professor.

'Login.pyw'
	janela de login para o programa de controle de notas, com o login e a senha que estão salvos dentro do arquivo professor.pck o usuario podera usar o software de controle de notas.

'Mw_control.pyw'
	janela principal do programa de controle de notas, nela existem duas opções de turmas, uma de ingles e uma de espanhol, ao clicar em um botão com o nome de uma das turmas o usuario é redirecionado para uma janela com uma lista de nomes de alunos para cadastro ou alteração dessa lista o usuario deve clicar sobre um dos botões verdes.

	apenas o nome, a nota e a presença de cada aluno poderão ser modificados atraves desses botões, o nivel é calculado automaticamente pois ele é a divisão da nota pelo numero de presenças que o aluno possuir.

	a opção NIVEL T foi um pedido extra da professora para que ela podesse escolher uma sigla de referencia para niveis que ela mesma podesse alterar.

'bd_al*.pck'
	são os arquivos que servem de banco dados para as informações sobre os alunos.