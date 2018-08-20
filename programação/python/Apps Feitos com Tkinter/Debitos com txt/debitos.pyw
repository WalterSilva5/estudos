import sys
import os.path
from tkinter import *
import subprocess

def janela():
    global tela, nomeClienteEntry, lbErro, lbAdicionarDebitos, entryAdicionarDebitos, btAdicionar, btVerlista, btLimparDebitos
    tela = Tk()
    tela.geometry("800x600+0+0")
    tela.configure(bg="black")
    tela.title("Sistema de Debitos.")

    nomeClienteLabel = Label(tela, text="Nome:", bg="black", fg="white", font=("arial",40,"bold"))
    nomeClienteLabel.place(x=20, y=10)
    nomeClienteEntry = Entry(tela, width="15", font=("arial",40,"bold"))
    nomeClienteEntry.place(x=190, y=10)

    lbErro = Label(tela, text="", bg="black", fg="white", font=("arial", 20, "bold"))
    lbErro.place(x=150,y=430)

    btVerificarDebitos=Button(tela, bg="red", fg="white", text="Verificar\nDebitos", font=("arial",20,"bold"), command=verificaClienteParaVerDebitos)
    btVerificarDebitos.place(x=20, y=150)
    btAdicionarCliente = Button(tela, bg="red", fg="white", text="Adicionar\nCliente", font=("arial",20,"bold"), command=verificaClienteCadastro)
    btAdicionarCliente.place(x=250,y=150)
    btAdicionarDebitosCliente = Button(tela, bg="red", fg="white", text="Adicionar\nDebitos", font=("arial", 20, "bold"),command=ativarBotaoAdicionarDebitos)
    btAdicionarDebitosCliente.place(x=500, y=150)
    btSair = Button(tela, bg="red", fg="white", text="Sair", font=("arial", 20, "bold"), command=sair)
    btSair.place(x=690, y=555)

    lbAdicionarDebitos=Label(tela, text="Digite Debitos Para Adicionar(ex: 2+2+3)", bg="white", fg="black", font=("arial",15,"bold"))

    entryAdicionarDebitos=Entry(tela, width="28", bg ="white", font=("arial",35,"bold"))
    btAdicionar = Button(tela, bg="red", fg="white", text="Adicionar", font=("arial", 20, "bold"),command=verificaClienteParaAdicionarDebitos)
    btVerlista =  Button(tela, bg="red", fg="white", text="Ver Lista De Debitos", font=("arial", 20, "bold"), command = verListaDeDebitos)
    btLimparDebitos =  Button(tela, bg="red", fg="white", text="Limpar Debitos", font=("arial", 20, "bold"), command = limparDebitos)



    btAbrirCalculadora= Button(tela, bg="red", fg="white", text="Abrir Calculadora", font=("arial",20,"bold"), command=telaCalculadora)
    btAbrirCalculadora.place(x=200,y=555)
    tela.mainloop()


def sair():
    tela.destroy()

def limparDebitos():
    nome = nomeClienteEntry.get()
    try:
        os.remove("{}.txt".format(nome))
        lbErro["text"]="Debitos apagados"
        arquivo = open("{}.txt".format(nome), "w")
        arquivo.write("0")
        arquivo.close()
    except:
        lbErro["text"]="Cliente não cadastrado"
        pass
 
    
def telaCalculadora():
    os.startfile("calc.exe")

def verListaDeDebitos():
    nome = nomeClienteEntry.get()
    subprocess.Popen("{} {}".format("notepad.exe", "{}.txt".format(nome)))
    
def verificaClienteParaVerDebitos():
    nome = nomeClienteEntry.get()
    if not os.path.exists(nome + '.txt'):
        lbErro["text"]="Cliente não esta cadastrado\nCliente em cadastrar caso queira."

    elif os.path.exists(nome+'.txt'):
        verDebitosCliente()

def verDebitosCliente():
    """Mostra os debitos do cliente salvos no arquivo do cliente"""
    nome=nomeClienteEntry.get()
    arquivo = open('{}.txt'.format(nome), 'r')
    debitos = arquivo.read()
    arquivo.close()
    debitos = debitos.split('\n')
    valor = 0
    for x in range(len(debitos)):
        try:
            valor += float(debitos[x])
        except:
            continue
    lbErro["text"] = "No total o cliente {} deve R${:.2f}".format(nome, valor)


def verificaClienteCadastro():
    nome = nomeClienteEntry.get()
    """verifica se o cliente ja encontra-se cadastrado se não estiver cadastrado """
    if os.path.exists(nome + '.txt'):
        lbErro["text"]=('{} ja esta cadastrado'.format(nome))
    else :
        salvaCliente(nome)


def salvaCliente(nome):
    """Salva o cliente em um arquivo para edição posterior"""
    nome = nomeClienteEntry.get()
    arquivo = open('{}.txt'.format(nome), 'w')
    arquivo.write('0')
    arquivo.close()
    lbErro["text"]=("Cliente {} Cadastrado Com Sucesso.".format(nome))

def ativarBotaoAdicionarDebitos():
    lbAdicionarDebitos.place(x=20,y=250)
    entryAdicionarDebitos.place(x=20,y=300)
    btAdicionar.place(x=20,y=380)
    btVerlista.place(x=350,y=380)
    btLimparDebitos.place(x=50,y=480)    

def verificaClienteParaAdicionarDebitos():
    nome = nomeClienteEntry.get()
    if not os.path.exists(nome + '.txt'):
        lbErro["text"]="Cliente não esta cadastrado, Favor Verificar."
    elif os.path.exists(nome+'.txt'):
        adicionarDebitosCliente()



def adicionarDebitosCliente():
    nome= nomeClienteEntry.get()
    arquivo = open('{}.txt'.format(nome), 'r')
    debitos = arquivo.read()
    arquivo.close()

    debitos = debitos.split('\n')
    valor = 0
    for x in range(len(debitos)):
        try:
            valor += float(debitos[x])
        except ValueError:
            arquivo = open(nome + ".txt", "w")
            arquivo.write('0')
            arquivo.close()

    novosDebitos=entryAdicionarDebitos.get()
    novosDebitos=novosDebitos.split("+")

    arquivo = open("{}.txt".format(nome),"w")
    for x in range(len(novosDebitos)):
        try:
            debitos.append(str(float(novosDebitos[x])))
        except :
            continue

    for x in range(len(debitos)):
        arquivo.write(debitos[x]+"\n")
    arquivo.close()
    lbErro["text"]="Debitos adicionados ao cliente {}.\n\n".format(nome)


janela()
