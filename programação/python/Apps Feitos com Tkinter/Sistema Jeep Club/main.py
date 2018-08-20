from tkinter import *
class LoginScreen():
    def __init__(self, root):
        root.geometry("800x600+100+100")

        categoria_campeonato = IntVar()
        categoria_jeep = IntVar()

        #escolha da categoria do campeonado que o participante vai entrar
        self.form_categorias = Frame(root).pack()
        self.texto_categorias_campeonato = Label(self.form_categorias, text = "CATEGORIA DE CAMPEONATO", fg="red",font=
        "arial 20 bold").place(x=0, y=0)
        self.categoria_1 = Radiobutton(self.form_categorias, text = "NACIONAL", variable=categoria_campeonato, fg="green", font="arial 15 bold").place(x=0, y=40)
        self.categoria_3 = Radiobutton(self.form_categorias, text = "REGIONAL", variable=categoria_campeonato, fg="green", font="arial 15 bold").place(x=150, y=40)
        self.categoria_2 = Radiobutton(self.form_categorias, text = "LOCAL", variable=categoria_campeonato, fg="green",  font="arial 15 bold").place(x=300, y=40)

        #escolha do tipo de jeep do participante
        self.texto_categorias_jeep= Label(self.form_categorias, text="CATEGORIA DE VEICULO", fg="red",font="arial 20 bold").place(x=0, y=80)
        self.jeep_1 = Radiobutton(self.form_categorias, text="jeep1", variable = categoria_jeep, fg="green", font="arial 15 bold").place(x=0, y=120)
        self.jeep_2 = Radiobutton(self.form_categorias, text="jeep2", variable = categoria_jeep, fg="green", font="arial 15 bold").place(x=80, y=120)
        self.jeep_3 = Radiobutton(self.form_categorias, text="jeep3", variable = categoria_jeep, fg="green", font="arial 15 bold").place(x=160, y=120)
        self.jeep_4 = Radiobutton(self.form_categorias, text="jeep4", variable = categoria_jeep, fg="green", font="arial 15 bold").place(x=240, y=120)

        #formulario com informações escritas do participante
        self.form_infos = Frame(root).pack()
        self.text_infos = Label(self.form_infos, text="INFORMAÇÕES DO PARTICIPANTE", fg="blue",font="arial 20 bold").place(x=0, y=180)

        #entrada de nome do piloto
        self.text_pioloto = Label(self.form_infos, text="PILOTO:", fg="red", font="arial 15 bold").place(x=0, y=220)
        self.entrada_piloto= Entry(self.form_infos, width="60",font="arial 15 bold")
        self.entrada_piloto.place(x=90, y=220)

        #entrada de nome do co-piloto
        self.text_co_pioloto = Label(self.form_infos, text="CO-PILOTO:", fg="red", font="arial 15 bold").place(x=0, y=255)
        self.entrada_co_piloto= Entry(self.form_infos, width="57",font="arial 15 bold").place(x=125, y=255)

        #APELIDO
        self.text_apelido = Label(self.form_infos, text="APELIDO:", fg="red",font="arial 15 bold").place(x=0, y=290)
        self.entrada_apelido = Entry(self.form_infos, width = 20, font="arial 15 bold").place(x=100, y=290)

        #CIDADE
        self.text_cidade = Label(self.form_infos, text="CIDADE:",fg="red", font="arial 15 bold").place(x=340, y= 290)
        self.entrada_cidade = Entry(self.form_infos, width=29, font="arial 15 bold").place(x=430, y=290)

        self.salvar = Button(root, text = "SALVAR", bg="#00ffff", font="arial 30 bold", command = self.salva).place(x=600,y=500)

    def salva(self):
        print(self.entrada_piloto.get())

root = Tk()
root.title = ("CADASTRO DE PARTICIPANTES")
tela = LoginScreen(root)
root.mainloop()