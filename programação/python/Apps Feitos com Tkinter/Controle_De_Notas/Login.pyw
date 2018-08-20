from Mw_control import *
from tkinter import *
import pickle

def testa():
    global telat,et_login, et_senha,lb_erro_login, lb_erro_senha

    login = et_login.get()
    senha = et_senha.get()


    arquivo = open('professor.pck', 'rb')
    professor = pickle.load(arquivo)

    login1 = professor["login"]
    senha1 = professor["senha"]
    arquivo.close()

    if login != login1:
        lb_erro_login["text"]="ERRO! Login Invalido, Tente Novamente"
        lb_erro_login["bg"]="red"
        raise Exception

    if senha != senha1:
        lb_erro_senha["text"]="ERRO! Senha Invalida, Tente Novamente"
        lb_erro_senha["bg"]="red"
        raise Exception

    if login1 == login and senha == senha1:
        telat.destroy()
        escolha_turmas()

    else:
        print("ERRO")
        raise Exception


def Tela():
    """Tela de login do MW control"""
    global telat, et_login, et_senha, lb_erro_login, lb_erro_senha
    telat = Tk()
    telat.geometry("355x180+500+200")
    telat.title("Login - MW Control")
    telat.configure(bg="white")

    et_login = Entry(telat,width = '30', font="Arial, 15")
    et_login.place(x=10, y=30)
    et_senha = Entry(telat,width = '30', show="*", font="Arial, 15")
    et_senha.place(x=10, y=70)

    lb_erro_login = Label(telat, text="Digite o Login e a Senha do professor", bg="green", fg="white", font="Arial, 12")
    lb_erro_login.place(x=45, y=100)
    lb_erro_senha = Label(telat, text="Digite o Login e a Senha do professor", bg="green", fg="white", font="Arial, 12")
    lb_erro_senha.place(x=45, y=100)

    bt_abre = Button(telat, text="Logar", bg="blue", fg="white", font="Arial, 20", command=testa)
    bt_abre.place(x=130, y=130)
    telat.mainloop()


Tela()