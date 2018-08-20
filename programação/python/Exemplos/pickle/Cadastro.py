import pickle

def inicial():
    op = input("Digite v para ver dados do usuario ou c para cadastrar novo usuario: ").lower()
    if op == 'v':
        ver()
    elif op == 'c':
        nome = input("Digite seu nome")
        senha = input("Digite sua senha")
        cadastro(nome,senha)
    else:
        print("opeção invalida")
        inicial()

def cadastro(nome,senha):

    usuario = {"nome":nome,"senha":senha}

    arquivo = open("usuario.pck","wb")
    pickle.dump(usuario,arquivo)
    arquivo.close()
    print("Cadastrado")
    inicial()

def ver():
    arquivo = open("usuario.pck","rb")
    usuario = pickle.load(arquivo)
    arquivo.close()

    print(usuario["nome"],usuario["senha"])

inicial()