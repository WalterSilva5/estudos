from tkinter import *

class Janela():
    def __init__(self):
        self.tela = Tk()
        self.tela.geometry("800x600")
        self.tela.title("Login e Senha")
        self.label_nome = Label(self.tela, text="Login:", font="Arial 20 bold").place(x=50, y=100)
        self.entrada_nome = Entry(self.tela, font="Arial 20 bold").place(x=150, y=100)

        self.label_senha= Label(self.tela, text="Senha:", font="Arial 20 bold").place(x=50, y=150)
        self.entrada_senha = Entry(self.tela, font="Arial 20 bold").place(x=150, y=150)

        self.botao_logar = Button(self.tela, text="Logar", bg="green", font="Arial 20 bold", ).place(x=300, y=200)
        self.alerta = Label(self.tela, text="", font="Arial 20 bold").place(x=100, y=300)

        self.tela.mainloop()

