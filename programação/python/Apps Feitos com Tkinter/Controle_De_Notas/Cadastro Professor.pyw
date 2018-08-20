"""Programa para criar login e senha do professor do mw control
    apenas o professor deve ter acesso a essa interface
"""
from tkinter import *
import pickle

def salva():
	#função que salva no arquivo  professor.pck  o login e a senha
    global telat,et_login, et_senha,bt_salva
    bt_salva["text"]="SALVO!"
    bt_salva["bg"]="green"
    login = et_login.get()
    senha = et_senha.get()

    arquivo = open('professor.pck', 'wb')
    prof = {"login": login, "senha": senha}

    pickle.dump(prof, arquivo)
    arquivo.close()


def fecha():
    #função que fecha a janela de entrada de dados
    global telat

    telat.destroy()


def Tela():
	#tela de entrada de dados sobre o professor
    global telat,et_login, et_senha,lbl_msg,bt_salva
    telat = Tk()
    telat.geometry("355x180+500+200")
    telat.title("Cadastro Professor - MW Control")
    telat.configure(bg="white")

    et_login = Entry(telat, width='30', font="Arial, 15")
    et_login.place(x=10, y=30)
    et_senha = Entry(telat, width='30', show="*", font="Arial, 15")
    et_senha.place(x=10, y=70)

    lbl_msg = Label(telat, text="Digite o Login e a Senha do professor para cadastrar", fg="white", bg="green",font=("Arial, 10"))
    lbl_msg.place(x=23, y=100)

    bt_salva = Button(telat, text="Salvar", bg="blue", fg="white", font="Arial, 20", command = salva)
    bt_salva.place(x=130, y=130)

    bt_fecha = Button(telat, text="Fechar", bg="black", fg="white", font="Arial, 15", command = fecha)
    bt_fecha.place(x=250, y=130)

    telat.mainloop()


Tela()