from tkinter import *
import pickle

""" Programa de gerenciamento de turmas de ingles e espanhol do curso de reforço
    com cadastro de nome, notas, presenças e nivel de cada aluno"""


def escolha_turmas():
    """tela inicial na qual o usuario escolhe uma das opções entre:
        escolha da turma para gerenciar alunos
        opção fazer backup dos arquivos do sistema"""

    global janela_escolha_de_turma

    janela_escolha_de_turma = Tk()	
    janela_escolha_de_turma.configure(background='white')
    janela_escolha_de_turma.title("Mw Control - Escolha De Turmas")

    img = PhotoImage(file='MWCONTROL.png')
    imagem = Label(janela_escolha_de_turma, image=img)
    imagem.place(x=160, y=110)

    bt_turma_ingles = Button(janela_escolha_de_turma, text="Turma de Inglês", fg="white", bg="blue", width=20, height=2,
                             font="Serif, 20", command=turma_ingles)
    bt_turma_ingles.place(x=150, y=10)

    bt_turma_espanhol = Button(janela_escolha_de_turma, text="Turma de Espanhol", fg="white", bg="green", width=20, height=2, font="Serif, 20", command = turma_espanhol)
    bt_turma_espanhol.place(x=150, y=220)

    janela_escolha_de_turma.geometry("600x300+450+200")
    janela_escolha_de_turma.mainloop()


###################################################################

def escolha_turmas2():
    """tela inicial na qual o usuario escolhe uma das opções entre:
        escolha da turma para gerenciar alunos
        opção fazer backup dos arquivos do sistema"""

    global janela_escolha_de_turma, janela_turma_ingles, janela_turma_espanhol, nivelt_ing1, lbl_nivelt_al_ing1
    janela_turma_ingles.destroy()

    janela_escolha_de_turma = Tk()
    janela_escolha_de_turma.configure(background='white')
    janela_escolha_de_turma.title("Mw Control - Escolha De Turmas")

    img = PhotoImage(file='MWCONTROL.png')
    imagem = Label(janela_escolha_de_turma, image=img)
    imagem.place(x=160, y=110)

    bt_turma_ingles = Button(janela_escolha_de_turma, text="Turma de Inglês", fg="white", bg="blue", width=20, height=2,
                             font="Serif, 20", command=turma_ingles)
    bt_turma_ingles.place(x=150, y=10)

    bt_turma_espanhol = Button(janela_escolha_de_turma, text="Turma de Espanhol", fg="white", bg="green", width=20, height=2, font="Serif, 20", command = turma_espanhol)
    bt_turma_espanhol.place(x=150, y=220)

    janela_escolha_de_turma.geometry("600x300+450+200")
    janela_escolha_de_turma.mainloop()


###################################################################
def escolha_turmas3():
    """tela inicial na qual o usuario escolhe uma das opções entre:
        escolha da turma para gerenciar alunos
        opção fazer backup dos arquivos do sistema"""

    global janela_escolha_de_turma, janela_turma_ingles, janela_turma_espanhol, nivelt_ing1, lbl_nivelt_al_ing1
    janela_turma_espanhol.destroy()
    
    janela_escolha_de_turma = Tk()
    janela_escolha_de_turma.configure(background='white')
    janela_escolha_de_turma.title("Mw Control - Escolha De Turmas")

    img = PhotoImage(file='MWCONTROL.png')
    imagem = Label(janela_escolha_de_turma, image=img)
    imagem.place(x=160, y=110)

    bt_turma_ingles = Button(janela_escolha_de_turma, text="Turma de Inglês", fg="white", bg="blue", width=20, height=2,
                             font="Serif, 20", command=turma_ingles)
    bt_turma_ingles.place(x=150, y=10)

    bt_turma_espanhol = Button(janela_escolha_de_turma, text="Turma de Espanhol", fg="white", bg="green", width=20, height=2, font="Serif, 20", command = turma_espanhol)
    bt_turma_espanhol.place(x=150, y=220)

    janela_escolha_de_turma.geometry("600x300+450+200")
    janela_escolha_de_turma.mainloop()


###################################################################


###################################################################


def turma_ingles():
    """tela para escolha dos alunos de ingles"""
    global janela_escolha_de_turma
    janela_escolha_de_turma.destroy()
    ################################################################
    global lbl_nv_al_ing1, lbl_nivelt_al_ing1, lbl_nome_al_ing1, janela_turma_ingles, lbl_nota_al_ing1, presenc_al_ing1, lbl_presenc_al_ing1
    global lbl_nv_al_ing2, lbl_nivelt_al_ing2, lbl_nome_al_ing2, janela_turma_ingles, lbl_nota_al_ing2, presenc_al_ing2, lbl_presenc_al_ing2
    global lbl_nv_al_ing3, lbl_nivelt_al_ing3, lbl_nome_al_ing3, janela_turma_ingles, lbl_nota_al_ing3, presenc_al_ing3, lbl_presenc_al_ing3
    global lbl_nv_al_ing4, lbl_nivelt_al_ing4, lbl_nome_al_ing4, janela_turma_ingles, lbl_nota_al_ing4, presenc_al_ing4, lbl_presenc_al_ing4
    global lbl_nv_al_ing5, lbl_nivelt_al_ing5, lbl_nome_al_ing5, janela_turma_ingles, lbl_nota_al_ing5, presenc_al_ing5, lbl_presenc_al_ing5
    global lbl_nv_al_ing6, lbl_nivelt_al_ing6, lbl_nome_al_ing6, janela_turma_ingles, lbl_nota_al_ing6, presenc_al_ing6, lbl_presenc_al_ing6
    global lbl_nv_al_ing7, lbl_nivelt_al_ing7, lbl_nome_al_ing7, janela_turma_ingles, lbl_nota_al_ing7, presenc_al_ing7, lbl_presenc_al_ing7
    global lbl_nv_al_ing8, lbl_nivelt_al_ing8, lbl_nome_al_ing8, janela_turma_ingles, lbl_nota_al_ing8, presenc_al_ing8, lbl_presenc_al_ing8
    global lbl_nv_al_ing9, lbl_nivelt_al_ing9, lbl_nome_al_ing9, janela_turma_ingles, lbl_nota_al_ing9, presenc_al_ing9, lbl_presenc_al_ing9
    global lbl_nv_al_ing10, lbl_nivelt_al_ing10, lbl_nome_al_ing10, janela_turma_ingles, lbl_nota_al_ing10, presenc_al_ing10, lbl_presenc_al_ing10

    ################################################################

    janela_turma_ingles = Tk()
    janela_turma_ingles.title("Mw Control - Turma de ingles")
    janela_turma_ingles.configure(bg="#bcf5ff")
    janela_turma_ingles.geometry("1280x600+50+100")

    # botão de voltar pra tela anterior
    voltar = Button(janela_turma_ingles, text="Voltar <-- ", width=7, bg="red", fg="white",
                    font=('Arial', '13', 'bold'), command=escolha_turmas2)
    voltar.place(x=20, y=0)

    # estrutura dedicada ao aluno 1 de ingles
    #####################################################################
    # botão que muda o nome do aluno 1 de ingles
    add_al_ing1 = Button(janela_turma_ingles, bg="green", fg="white", width=6, height=1, text="Aluno 1:",
                         font="Arial, 15", command=nome_al_ing1)

    # ve o label nome do aluno 1 de ingles no banco de dados

    arquivo = open('bd_al_ing1.pck', 'rb')
    bd_al_ing1 = pickle.load(arquivo)

    txt_nome_al_ing1 = bd_al_ing1["nome"]
    txt_nota_al_ing1 = bd_al_ing1["nota"]
    txt_presenc_al_ing1 = bd_al_ing1["presenc"]
    nivelt = bd_al_ing1["nivelt"]
    nv_al_ing1 = int(bd_al_ing1["nota"]) // 2
    arquivo.close()

    # label com o nome do aluno 1 de ingles
    lbl_nome_al_ing1 = Label(janela_turma_ingles, text=txt_nome_al_ing1, bg="white", font="Arial, 15")

    # botão que muda a nota do aluno 1 de ingles
    add_nota_ing1 = Button(janela_turma_ingles, bg="green", fg="white", width=6, height=1, text="Nota: ",
                           font="Arial, 15", command=nota_al_ing1)

    # label com a nota do aluno 1 de ingles
    lbl_nota_al_ing1 = Label(janela_turma_ingles, text=txt_nota_al_ing1, bg="white", font="Arial, 15")

    # botão que muda a presença do aluno 1 de ingles
    presenc_al_ing1 = Button(janela_turma_ingles, bg="green", fg="white", width=8, height=1, text="Presenças: ",
                             font="Arial, 15", command=presenc_al_ing1)

    # label com a presença do aluno 1 de ingles
    lbl_presenc_al_ing1 = Label(janela_turma_ingles, text=txt_presenc_al_ing1, bg="white", font="Arial, 15")

    # label com o nome nivel do aluno 1 de ingles
    lbl_nome_nv_al_ing1 = Label(janela_turma_ingles, text="Nivel:", width=6, bg="green", fg="white", font="Arial, 17")

    # label com o  nivel do aluno 1 de ingles
    lbl_nv_al_ing1 = Label(janela_turma_ingles, text=nv_al_ing1, bg="white", font="Arial, 17")

    # botão que muda o nome nivel de turma do aluno 1 de ingles
    bt_nv_turma_al_ing1 = Button(janela_turma_ingles, bg="green", fg="white", width=6, height=1, text="Nivel T: ",
                                 font="Arial, 15", command=nivelt_al_ing1)

    # label com o nivel de turma do aluno 1 de ingles
    lbl_nivelt_al_ing1 = Label(janela_turma_ingles, text=nivelt, bg="white", font="Arial, 17")

    # posicionamento dos objetos do aluno 1
    add_al_ing1.place(x=20, y=40)
    lbl_nome_al_ing1.place(x=120, y=45)

    add_nota_ing1.place(x=600, y=40)
    lbl_nota_al_ing1.place(x=700, y=45)

    presenc_al_ing1.place(x=770, y=40)
    lbl_presenc_al_ing1.place(x=900, y=45)

    lbl_nome_nv_al_ing1.place(x=950, y=45)
    lbl_nv_al_ing1.place(x=1050, y=45)

    bt_nv_turma_al_ing1.place(x=1100, y=40)
    lbl_nivelt_al_ing1.place(x=1205, y=45)

    #####################################################################
    # fim da estrutura do aluno 1
    #####################################################################

    #####################################################################
    #####################################################################
    #####################################################################

    # estrutura dedicada ao aluno 2 de ingles
    #####################################################################
    # botão que muda o nome do aluno 2 de ingles
    add_al_ing2 = Button(janela_turma_ingles, bg="green", fg="white", width=6, height=1, text="aluno 2:",
                         font="Arial, 15", command=nome_al_ing2)

    # ve o label nome do aluno 2 de ingles no banco de dados

    arquivo = open('bd_al_ing2.pck', 'rb')
    bd_al_ing2 = pickle.load(arquivo)

    txt_nome_al_ing2 = bd_al_ing2["nome"]
    txt_nota_al_ing2 = bd_al_ing2["nota"]
    txt_presenc_al_ing2 = bd_al_ing2["presenc"]
    nivelt = bd_al_ing2["nivelt"]
    nv_al_ing2 = int(bd_al_ing2["nota"]) // 2
    arquivo.close()

    # label com o nome do aluno 2 de ingles
    lbl_nome_al_ing2 = Label(janela_turma_ingles, text=txt_nome_al_ing2, bg="white", font="Arial, 15")

    # botão que muda a nota do aluno 2 de ingles
    add_nota_ing2 = Button(janela_turma_ingles, bg="green", fg="white", width=6, height=1, text="Nota: ",
                           font="Arial, 15", command=nota_al_ing2)

    # label com a nota do aluno 2 de ingles
    lbl_nota_al_ing2 = Label(janela_turma_ingles, text=txt_nota_al_ing2, bg="white", font="Arial, 15")

    # botão que muda a presença do aluno 2 de ingles
    presenc_al_ing2 = Button(janela_turma_ingles, bg="green", fg="white", width=8, height=1, text="Presenças: ",
                             font="Arial, 15", command=presenc_al_ing2)

    # label com a presença do aluno 2 de ingles
    lbl_presenc_al_ing2 = Label(janela_turma_ingles, text=txt_presenc_al_ing2, bg="white", font="Arial, 15")

    # label com o nome nivel do aluno 2 de ingles
    lbl_nome_nv_al_ing2 = Label(janela_turma_ingles, text="Nivel:", width=6, bg="green", fg="white", font="Arial, 17")

    # label com o  nivel do aluno 2 de ingles
    lbl_nv_al_ing2 = Label(janela_turma_ingles, text=nv_al_ing2, bg="white", font="Arial, 17")

    # botão que muda o nome nivel de turma do aluno 2 de ingles
    bt_nv_turma_al_ing2 = Button(janela_turma_ingles, bg="green", fg="white", width=6, height=1, text="Nivel T: ",
                                 font="Arial, 15", command=nivelt_al_ing2)

    # label com o nivel de turma do aluno 2 de ingles
    lbl_nivelt_al_ing2 = Label(janela_turma_ingles, text=nivelt, bg="white", font="Arial, 17")

    # posicionamento dos objetos do aluno 2
    add_al_ing2.place(x=20, y=90)
    lbl_nome_al_ing2.place(x=120, y=95)

    add_nota_ing2.place(x=600, y=90)
    lbl_nota_al_ing2.place(x=700, y=95)

    presenc_al_ing2.place(x=770, y=90)
    lbl_presenc_al_ing2.place(x=900, y=95)

    lbl_nome_nv_al_ing2.place(x=950, y=95)
    lbl_nv_al_ing2.place(x=1050, y=95)

    bt_nv_turma_al_ing2.place(x=1100, y=90)
    lbl_nivelt_al_ing2.place(x=1205, y=95)
    #####################################################################
    # fim da estrutura do aluno 2
    #####################################################################

    #####################################################################
    #####################################################################
    #####################################################################

    # estrutura dedicada ao aluno 3 de ingles
    #####################################################################
    # botão que muda o nome do aluno 3 de ingles
    add_al_ing3 = Button(janela_turma_ingles, bg="green", fg="white", width=6, height=1, text="aluno 3:",
                         font="Arial, 15", command=nome_al_ing3)

    # ve o label nome do aluno 3 de ingles no banco de dados

    arquivo = open('bd_al_ing3.pck', 'rb')
    bd_al_ing3 = pickle.load(arquivo)

    txt_nome_al_ing3 = bd_al_ing3["nome"]
    txt_nota_al_ing3 = bd_al_ing3["nota"]
    txt_presenc_al_ing3 = bd_al_ing3["presenc"]
    nivelt = bd_al_ing3["nivelt"]
    nv_al_ing3 = int(bd_al_ing3["nota"]) // 2
    arquivo.close()

    # label com o nome do aluno 3 de ingles
    lbl_nome_al_ing3 = Label(janela_turma_ingles, text=txt_nome_al_ing3, bg="white", font="Arial, 15")

    # botão que muda a nota do aluno 3 de ingles
    add_nota_ing3 = Button(janela_turma_ingles, bg="green", fg="white", width=6, height=1, text="Nota: ",
                           font="Arial, 15", command=nota_al_ing3)

    # label com a nota do aluno 3 de ingles
    lbl_nota_al_ing3 = Label(janela_turma_ingles, text=txt_nota_al_ing3, bg="white", font="Arial, 15")

    # botão que muda a presença do aluno 3 de ingles
    presenc_al_ing3 = Button(janela_turma_ingles, bg="green", fg="white", width=8, height=1, text="Presenças: ",
                             font="Arial, 15", command=presenc_al_ing3)

    # label com a presença do aluno 3 de ingles
    lbl_presenc_al_ing3 = Label(janela_turma_ingles, text=txt_presenc_al_ing3, bg="white", font="Arial, 15")

    # label com o nome nivel do aluno 3 de ingles
    lbl_nome_nv_al_ing3 = Label(janela_turma_ingles, text="Nivel:", width=6, bg="green", fg="white", font="Arial, 17")

    # label com o  nivel do aluno 3 de ingles
    lbl_nv_al_ing3 = Label(janela_turma_ingles, text=nv_al_ing3, bg="white", font="Arial, 17")

    # botão que muda o nome nivel de turma do aluno 3 de ingles
    bt_nv_turma_al_ing3 = Button(janela_turma_ingles, bg="green", fg="white", width=6, height=1, text="Nivel T: ",
                                 font="Arial, 15", command=nivelt_al_ing3)

    # label com o nivel de turma do aluno 3 de ingles
    lbl_nivelt_al_ing3 = Label(janela_turma_ingles, text=nivelt, bg="white", font="Arial, 17")

    # posicionamento dos objetos do aluno 3
    add_al_ing3.place(x=20, y=140)
    lbl_nome_al_ing3.place(x=120, y=145)

    add_nota_ing3.place(x=600, y=140)
    lbl_nota_al_ing3.place(x=700, y=145)

    presenc_al_ing3.place(x=770, y=140)
    lbl_presenc_al_ing3.place(x=900, y=145)

    lbl_nome_nv_al_ing3.place(x=950, y=145)
    lbl_nv_al_ing3.place(x=1050, y=145)

    bt_nv_turma_al_ing3.place(x=1100, y=140)
    lbl_nivelt_al_ing3.place(x=1205, y=145)
    #####################################################################
    # fim da estrutura do aluno 3
    #####################################################################

    #####################################################################
    #####################################################################
    #####################################################################

    # estrutura dedicada ao aluno 4 de ingles
    #####################################################################
    # botão que muda o nome do aluno 4 de ingles
    add_al_ing4 = Button(janela_turma_ingles, bg="green", fg="white", width=6, height=1, text="aluno 4:",
                         font="Arial, 15", command=nome_al_ing4)

    # ve o label nome do aluno 4 de ingles no banco de dados

    arquivo = open('bd_al_ing4.pck', 'rb')
    bd_al_ing4 = pickle.load(arquivo)

    txt_nome_al_ing4 = bd_al_ing4["nome"]
    txt_nota_al_ing4 = bd_al_ing4["nota"]
    txt_presenc_al_ing4 = bd_al_ing4["presenc"]
    nivelt = bd_al_ing4["nivelt"]
    nv_al_ing4 = int(bd_al_ing4["nota"]) // 2
    arquivo.close()

    # label com o nome do aluno 4 de ingles
    lbl_nome_al_ing4 = Label(janela_turma_ingles, text=txt_nome_al_ing4, bg="white", font="Arial, 15")

    # botão que muda a nota do aluno 4 de ingles
    add_nota_ing4 = Button(janela_turma_ingles, bg="green", fg="white", width=6, height=1, text="Nota: ",
                           font="Arial, 15", command=nota_al_ing4)

    # label com a nota do aluno 4 de ingles
    lbl_nota_al_ing4 = Label(janela_turma_ingles, text=txt_nota_al_ing4, bg="white", font="Arial, 15")

    # botão que muda a presença do aluno 4 de ingles
    presenc_al_ing4 = Button(janela_turma_ingles, bg="green", fg="white", width=8, height=1, text="Presenças: ",
                             font="Arial, 15", command=presenc_al_ing4)

    # label com a presença do aluno 4 de ingles
    lbl_presenc_al_ing4 = Label(janela_turma_ingles, text=txt_presenc_al_ing4, bg="white", font="Arial, 15")

    # label com o nome nivel do aluno 4 de ingles
    lbl_nome_nv_al_ing4 = Label(janela_turma_ingles, text="Nivel:", width=6, bg="green", fg="white", font="Arial, 17")

    # label com o  nivel do aluno 4 de ingles
    lbl_nv_al_ing4 = Label(janela_turma_ingles, text=nv_al_ing4, bg="white", font="Arial, 17")

    # botão que muda o nome nivel de turma do aluno 4 de ingles
    bt_nv_turma_al_ing4 = Button(janela_turma_ingles, bg="green", fg="white", width=6, height=1, text="Nivel T: ",
                                 font="Arial, 15", command=nivelt_al_ing4)

    # label com o nivel de turma do aluno 4 de ingles
    lbl_nivelt_al_ing4 = Label(janela_turma_ingles, text=nivelt, bg="white", font="Arial, 17")

    # posicionamento dos objetos do aluno 4
    add_al_ing4.place(x=20, y=200)
    lbl_nome_al_ing4.place(x=120, y=205)

    add_nota_ing4.place(x=600, y=200)
    lbl_nota_al_ing4.place(x=700, y=205)

    presenc_al_ing4.place(x=770, y=200)
    lbl_presenc_al_ing4.place(x=900, y=205)

    lbl_nome_nv_al_ing4.place(x=950, y=205)
    lbl_nv_al_ing4.place(x=1050, y=205)

    bt_nv_turma_al_ing4.place(x=1100, y=200)
    lbl_nivelt_al_ing4.place(x=1205, y=205)

    #####################################################################
    # fim da estrutura do aluno 4
    #####################################################################

    #####################################################################
    #####################################################################
    #####################################################################

    # estrutura dedicada ao aluno 5 de ingles
    #####################################################################
    # botão que muda o nome do aluno 5 de ingles
    add_al_ing5 = Button(janela_turma_ingles, bg="green", fg="white", width=6, height=1, text="aluno 5:",
                         font="Arial, 15", command=nome_al_ing5)

    # ve o label nome do aluno 5 de ingles no banco de dados

    arquivo = open('bd_al_ing5.pck', 'rb')
    bd_al_ing5 = pickle.load(arquivo)

    txt_nome_al_ing5 = bd_al_ing5["nome"]
    txt_nota_al_ing5 = bd_al_ing5["nota"]
    txt_presenc_al_ing5 = bd_al_ing5["presenc"]
    nivelt = bd_al_ing5["nivelt"]
    nv_al_ing5 = int(bd_al_ing5["nota"]) // 2
    arquivo.close()

    # label com o nome do aluno 5 de ingles
    lbl_nome_al_ing5 = Label(janela_turma_ingles, text=txt_nome_al_ing5, bg="white", font="Arial, 15")

    # botão que muda a nota do aluno 5 de ingles
    add_nota_ing5 = Button(janela_turma_ingles, bg="green", fg="white", width=6, height=1, text="Nota: ",
                           font="Arial, 15", command=nota_al_ing5)

    # label com a nota do aluno 5 de ingles
    lbl_nota_al_ing5 = Label(janela_turma_ingles, text=txt_nota_al_ing5, bg="white", font="Arial, 15")

    # botão que muda a presença do aluno 5 de ingles
    presenc_al_ing5 = Button(janela_turma_ingles, bg="green", fg="white", width=8, height=1, text="Presenças: ",
                             font="Arial, 15", command=presenc_al_ing5)

    # label com a presença do aluno 5 de ingles
    lbl_presenc_al_ing5 = Label(janela_turma_ingles, text=txt_presenc_al_ing5, bg="white", font="Arial, 15")

    # label com o nome nivel do aluno 5 de ingles
    lbl_nome_nv_al_ing5 = Label(janela_turma_ingles, text="Nivel:", width=6, bg="green", fg="white", font="Arial, 17")

    # label com o  nivel do aluno 5 de ingles
    lbl_nv_al_ing5 = Label(janela_turma_ingles, text=nv_al_ing5, bg="white", font="Arial, 17")

    # botão que muda o nome nivel de turma do aluno 5 de ingles
    bt_nv_turma_al_ing5 = Button(janela_turma_ingles, bg="green", fg="white", width=6, height=1, text="Nivel T: ",
                                 font="Arial, 15", command=nivelt_al_ing5)

    # label com o nivel de turma do aluno 5 de ingles
    lbl_nivelt_al_ing5 = Label(janela_turma_ingles, text=nivelt, bg="white", font="Arial, 17")

    # posicionamento dos objetos do aluno 5
    add_al_ing5.place(x=20, y=250)
    lbl_nome_al_ing5.place(x=120, y=255)

    add_nota_ing5.place(x=600, y=250)
    lbl_nota_al_ing5.place(x=700, y=255)

    presenc_al_ing5.place(x=770, y=250)
    lbl_presenc_al_ing5.place(x=900, y=255)

    lbl_nome_nv_al_ing5.place(x=950, y=255)
    lbl_nv_al_ing5.place(x=1050, y=255)

    bt_nv_turma_al_ing5.place(x=1100, y=250)
    lbl_nivelt_al_ing5.place(x=1205, y=255)

    #####################################################################
    # fim da estrutura do aluno 5
    #####################################################################

    #####################################################################
    #####################################################################
    #####################################################################

    # estrutura dedicada ao aluno 6 de ingles
    #####################################################################
    # botão que muda o nome do aluno 6 de ingles
    add_al_ing6 = Button(janela_turma_ingles, bg="green", fg="white", width=6, height=1, text="aluno 6:",
                         font="Arial, 15", command=nome_al_ing6)

    # ve o label nome do aluno 6 de ingles no banco de dados

    arquivo = open('bd_al_ing6.pck', 'rb')
    bd_al_ing6 = pickle.load(arquivo)

    txt_nome_al_ing6 = bd_al_ing6["nome"]
    txt_nota_al_ing6 = bd_al_ing6["nota"]
    txt_presenc_al_ing6 = bd_al_ing6["presenc"]
    nivelt = bd_al_ing6["nivelt"]
    nv_al_ing6 = int(bd_al_ing6["nota"]) // 2
    arquivo.close()

    # label com o nome do aluno 6 de ingles
    lbl_nome_al_ing6 = Label(janela_turma_ingles, text=txt_nome_al_ing6, bg="white", font="Arial, 15")

    # botão que muda a nota do aluno 6 de ingles
    add_nota_ing6 = Button(janela_turma_ingles, bg="green", fg="white", width=6, height=1, text="Nota: ",
                           font="Arial, 15", command=nota_al_ing6)

    # label com a nota do aluno 6 de ingles
    lbl_nota_al_ing6 = Label(janela_turma_ingles, text=txt_nota_al_ing6, bg="white", font="Arial, 15")

    # botão que muda a presença do aluno 6 de ingles
    presenc_al_ing6 = Button(janela_turma_ingles, bg="green", fg="white", width=8, height=1, text="Presenças: ",
                             font="Arial, 15", command=presenc_al_ing6)

    # label com a presença do aluno 6 de ingles
    lbl_presenc_al_ing6 = Label(janela_turma_ingles, text=txt_presenc_al_ing6, bg="white", font="Arial, 15")

    # label com o nome nivel do aluno 6 de ingles
    lbl_nome_nv_al_ing6 = Label(janela_turma_ingles, text="Nivel:", width=6, bg="green", fg="white", font="Arial, 17")

    # label com o  nivel do aluno 6 de ingles
    lbl_nv_al_ing6 = Label(janela_turma_ingles, text=nv_al_ing6, bg="white", font="Arial, 17")

    # botão que muda o nome nivel de turma do aluno 6 de ingles
    bt_nv_turma_al_ing6 = Button(janela_turma_ingles, bg="green", fg="white", width=6, height=1, text="Nivel T: ",
                                 font="Arial, 15", command=nivelt_al_ing6)

    # label com o nivel de turma do aluno 6 de ingles
    lbl_nivelt_al_ing6 = Label(janela_turma_ingles, text=nivelt, bg="white", font="Arial, 17")

    # posicionamento dos objetos do aluno 6
    add_al_ing6.place(x=20, y=300)
    lbl_nome_al_ing6.place(x=120, y=305)

    add_nota_ing6.place(x=600, y=300)
    lbl_nota_al_ing6.place(x=700, y=305)

    presenc_al_ing6.place(x=770, y=300)
    lbl_presenc_al_ing6.place(x=900, y=305)

    lbl_nome_nv_al_ing6.place(x=950, y=305)
    lbl_nv_al_ing6.place(x=1050, y=305)

    bt_nv_turma_al_ing6.place(x=1100, y=300)
    lbl_nivelt_al_ing6.place(x=1205, y=305)

    #####################################################################
    # fim da estrutura do aluno 6
    #####################################################################

    #####################################################################
    #####################################################################
    #####################################################################

    # estrutura dedicada ao aluno 7 de ingles
    #####################################################################
    # botão que muda o nome do aluno 7 de ingles
    add_al_ing7 = Button(janela_turma_ingles, bg="green", fg="white", width=6, height=1, text="aluno 7:",
                         font="Arial, 15", command=nome_al_ing7)

    # ve o label nome do aluno 7 de ingles no banco de dados

    arquivo = open('bd_al_ing7.pck', 'rb')
    bd_al_ing7 = pickle.load(arquivo)

    txt_nome_al_ing7 = bd_al_ing7["nome"]
    txt_nota_al_ing7 = bd_al_ing7["nota"]
    txt_presenc_al_ing7 = bd_al_ing7["presenc"]
    nivelt = bd_al_ing7["nivelt"]
    nv_al_ing7 = int(bd_al_ing7["nota"]) // 2
    arquivo.close()

    # label com o nome do aluno 7 de ingles
    lbl_nome_al_ing7 = Label(janela_turma_ingles, text=txt_nome_al_ing7, bg="white", font="Arial, 15")

    # botão que muda a nota do aluno 7 de ingles
    add_nota_ing7 = Button(janela_turma_ingles, bg="green", fg="white", width=6, height=1, text="Nota: ",
                           font="Arial, 15", command=nota_al_ing7)

    # label com a nota do aluno 7 de ingles
    lbl_nota_al_ing7 = Label(janela_turma_ingles, text=txt_nota_al_ing7, bg="white", font="Arial, 15")

    # botão que muda a presença do aluno 7 de ingles
    presenc_al_ing7 = Button(janela_turma_ingles, bg="green", fg="white", width=8, height=1, text="Presenças: ",
                             font="Arial, 15", command=presenc_al_ing7)

    # label com a presença do aluno 7 de ingles
    lbl_presenc_al_ing7 = Label(janela_turma_ingles, text=txt_presenc_al_ing7, bg="white", font="Arial, 15")

    # label com o nome nivel do aluno 7 de ingles
    lbl_nome_nv_al_ing7 = Label(janela_turma_ingles, text="Nivel:", width=6, bg="green", fg="white", font="Arial, 17")

    # label com o  nivel do aluno 7 de ingles
    lbl_nv_al_ing7 = Label(janela_turma_ingles, text=nv_al_ing7, bg="white", font="Arial, 17")

    # botão que muda o nome nivel de turma do aluno 7 de ingles
    bt_nv_turma_al_ing7 = Button(janela_turma_ingles, bg="green", fg="white", width=6, height=1, text="Nivel T: ",
                                 font="Arial, 15", command=nivelt_al_ing7)

    # label com o nivel de turma do aluno 7 de ingles
    lbl_nivelt_al_ing7 = Label(janela_turma_ingles, text=nivelt, bg="white", font="Arial, 17")

    # posicionamento dos objetos do aluno 7
    add_al_ing7.place(x=20, y=350)
    lbl_nome_al_ing7.place(x=120, y=355)

    add_nota_ing7.place(x=600, y=350)
    lbl_nota_al_ing7.place(x=700, y=355)

    presenc_al_ing7.place(x=770, y=350)
    lbl_presenc_al_ing7.place(x=900, y=355)

    lbl_nome_nv_al_ing7.place(x=950, y=355)
    lbl_nv_al_ing7.place(x=1050, y=355)

    bt_nv_turma_al_ing7.place(x=1100, y=350)
    lbl_nivelt_al_ing7.place(x=1205, y=355)

    #####################################################################
    # fim da estrutura do aluno 7
    #####################################################################

    #####################################################################
    #####################################################################
    #####################################################################

    # estrutura dedicada ao aluno 8 de ingles
    #####################################################################
    # botão que muda o nome do aluno 8 de ingles
    add_al_ing8 = Button(janela_turma_ingles, bg="green", fg="white", width=6, height=1, text="aluno 8:",
                         font="Arial, 15", command=nome_al_ing8)

    # ve o label nome do aluno 8 de ingles no banco de dados

    arquivo = open('bd_al_ing8.pck', 'rb')
    bd_al_ing8 = pickle.load(arquivo)

    txt_nome_al_ing8 = bd_al_ing8["nome"]
    txt_nota_al_ing8 = bd_al_ing8["nota"]
    txt_presenc_al_ing8 = bd_al_ing8["presenc"]
    nivelt = bd_al_ing8["nivelt"]
    nv_al_ing8 = int(bd_al_ing8["nota"]) // 2
    arquivo.close()

    # label com o nome do aluno 8 de ingles
    lbl_nome_al_ing8 = Label(janela_turma_ingles, text=txt_nome_al_ing8, bg="white", font="Arial, 15")

    # botão que muda a nota do aluno 8 de ingles
    add_nota_ing8 = Button(janela_turma_ingles, bg="green", fg="white", width=6, height=1, text="Nota: ",
                           font="Arial, 15", command=nota_al_ing8)

    # label com a nota do aluno 8 de ingles
    lbl_nota_al_ing8 = Label(janela_turma_ingles, text=txt_nota_al_ing8, bg="white", font="Arial, 15")

    # botão que muda a presença do aluno 8 de ingles
    presenc_al_ing8 = Button(janela_turma_ingles, bg="green", fg="white", width=8, height=1, text="Presenças: ",
                             font="Arial, 15", command=presenc_al_ing8)

    # label com a presença do aluno 8 de ingles
    lbl_presenc_al_ing8 = Label(janela_turma_ingles, text=txt_presenc_al_ing8, bg="white", font="Arial, 15")

    # label com o nome nivel do aluno 8 de ingles
    lbl_nome_nv_al_ing8 = Label(janela_turma_ingles, text="Nivel:", width=6, bg="green", fg="white", font="Arial, 17")

    # label com o  nivel do aluno 8 de ingles
    lbl_nv_al_ing8 = Label(janela_turma_ingles, text=nv_al_ing8, bg="white", font="Arial, 17")

    # botão que muda o nome nivel de turma do aluno 8 de ingles
    bt_nv_turma_al_ing8 = Button(janela_turma_ingles, bg="green", fg="white", width=6, height=1, text="Nivel T: ",
                                 font="Arial, 15", command=nivelt_al_ing8)

    # label com o nivel de turma do aluno 8 de ingles
    lbl_nivelt_al_ing8 = Label(janela_turma_ingles, text=nivelt, bg="white", font="Arial, 17")

    # posicionamento dos objetos do aluno 8
    add_al_ing8.place(x=20, y=400)
    lbl_nome_al_ing8.place(x=120, y=405)

    add_nota_ing8.place(x=600, y=400)
    lbl_nota_al_ing8.place(x=700, y=405)

    presenc_al_ing8.place(x=770, y=400)
    lbl_presenc_al_ing8.place(x=900, y=405)

    lbl_nome_nv_al_ing8.place(x=950, y=405)
    lbl_nv_al_ing8.place(x=1050, y=405)

    bt_nv_turma_al_ing8.place(x=1100, y=400)
    lbl_nivelt_al_ing8.place(x=1205, y=405)

    #####################################################################
    # fim da estrutura do aluno 8
    #####################################################################

    #####################################################################
    #####################################################################
    #####################################################################

    # estrutura dedicada ao aluno 9 de ingles
    #####################################################################
    # botão que muda o nome do aluno 9 de ingles
    add_al_ing9 = Button(janela_turma_ingles, bg="green", fg="white", width=6, height=1, text="aluno 9:",
                         font="Arial, 15", command=nome_al_ing9)

    # ve o label nome do aluno 9 de ingles no banco de dados

    arquivo = open('bd_al_ing9.pck', 'rb')
    bd_al_ing9 = pickle.load(arquivo)

    txt_nome_al_ing9 = bd_al_ing9["nome"]
    txt_nota_al_ing9 = bd_al_ing9["nota"]
    txt_presenc_al_ing9 = bd_al_ing9["presenc"]
    nivelt = bd_al_ing9["nivelt"]
    nv_al_ing9 = int(bd_al_ing9["nota"]) // 2
    arquivo.close()

    # label com o nome do aluno 9 de ingles
    lbl_nome_al_ing9 = Label(janela_turma_ingles, text=txt_nome_al_ing9, bg="white", font="Arial, 15")

    # botão que muda a nota do aluno 9 de ingles
    add_nota_ing9 = Button(janela_turma_ingles, bg="green", fg="white", width=6, height=1, text="Nota: ",
                           font="Arial, 15", command=nota_al_ing9)

    # label com a nota do aluno 9 de ingles
    lbl_nota_al_ing9 = Label(janela_turma_ingles, text=txt_nota_al_ing9, bg="white", font="Arial, 15")

    # botão que muda a presença do aluno 9 de ingles
    presenc_al_ing9 = Button(janela_turma_ingles, bg="green", fg="white", width=8, height=1, text="Presenças: ",
                             font="Arial, 15", command=presenc_al_ing9)

    # label com a presença do aluno 9 de ingles
    lbl_presenc_al_ing9 = Label(janela_turma_ingles, text=txt_presenc_al_ing9, bg="white", font="Arial, 15")

    # label com o nome nivel do aluno 9 de ingles
    lbl_nome_nv_al_ing9 = Label(janela_turma_ingles, text="Nivel:", width=6, bg="green", fg="white", font="Arial, 17")

    # label com o  nivel do aluno 9 de ingles
    lbl_nv_al_ing9 = Label(janela_turma_ingles, text=nv_al_ing9, bg="white", font="Arial, 17")

    # botão que muda o nome nivel de turma do aluno 9 de ingles
    bt_nv_turma_al_ing9 = Button(janela_turma_ingles, bg="green", fg="white", width=6, height=1, text="Nivel T: ",
                                 font="Arial, 15", command=nivelt_al_ing9)

    # label com o nivel de turma do aluno 9 de ingles
    lbl_nivelt_al_ing9 = Label(janela_turma_ingles, text=nivelt, bg="white", font="Arial, 17")

    # posicionamento dos objetos do aluno 9
    add_al_ing9.place(x=20, y=450)
    lbl_nome_al_ing9.place(x=120, y=455)

    add_nota_ing9.place(x=600, y=450)
    lbl_nota_al_ing9.place(x=700, y=455)

    presenc_al_ing9.place(x=770, y=450)
    lbl_presenc_al_ing9.place(x=900, y=455)

    lbl_nome_nv_al_ing9.place(x=950, y=455)
    lbl_nv_al_ing9.place(x=1050, y=455)

    bt_nv_turma_al_ing9.place(x=1100, y=450)
    lbl_nivelt_al_ing9.place(x=1205, y=455)

    #####################################################################
    # fim da estrutura do aluno 9
    #####################################################################

    #####################################################################
    #####################################################################
    #####################################################################

    # estrutura dedicada ao aluno 10 de ingles
    #####################################################################
    # botão que muda o nome do aluno 10 de ingles
    add_al_ing10 = Button(janela_turma_ingles, bg="green", fg="white", width=6, height=1, text="aluno 10:",
                         font="Arial, 15", command=nome_al_ing10)

    # ve o label nome do aluno 10 de ingles no banco de dados

    arquivo = open('bd_al_ing10.pck', 'rb')
    bd_al_ing10 = pickle.load(arquivo)

    txt_nome_al_ing10 = bd_al_ing10["nome"]
    txt_nota_al_ing10 = bd_al_ing10["nota"]
    txt_presenc_al_ing10 = bd_al_ing10["presenc"]
    nivelt = bd_al_ing10["nivelt"]
    nv_al_ing10 = int(bd_al_ing10["nota"]) // 2
    arquivo.close()

    # label com o nome do aluno 10 de ingles
    lbl_nome_al_ing10 = Label(janela_turma_ingles, text=txt_nome_al_ing10, bg="white", font="Arial, 15")

    # botão que muda a nota do aluno 10 de ingles
    add_nota_ing10 = Button(janela_turma_ingles, bg="green", fg="white", width=6, height=1, text="Nota: ",
                           font="Arial, 15", command=nota_al_ing10)

    # label com a nota do aluno 10 de ingles
    lbl_nota_al_ing10 = Label(janela_turma_ingles, text=txt_nota_al_ing10, bg="white", font="Arial, 15")

    # botão que muda a presença do aluno 10 de ingles
    presenc_al_ing10 = Button(janela_turma_ingles, bg="green", fg="white", width=8, height=1, text="Presenças: ",
                             font="Arial, 15", command=presenc_al_ing10)

    # label com a presença do aluno 10 de ingles
    lbl_presenc_al_ing10 = Label(janela_turma_ingles, text=txt_presenc_al_ing10, bg="white", font="Arial, 15")

    # label com o nome nivel do aluno 10 de ingles
    lbl_nome_nv_al_ing10 = Label(janela_turma_ingles, text="Nivel:", width=6, bg="green", fg="white", font="Arial, 17")

    # label com o  nivel do aluno 10 de ingles
    lbl_nv_al_ing10 = Label(janela_turma_ingles, text=nv_al_ing10, bg="white", font="Arial, 17")

    # botão que muda o nome nivel de turma do aluno 10 de ingles
    bt_nv_turma_al_ing10 = Button(janela_turma_ingles, bg="green", fg="white", width=6, height=1, text="Nivel T: ", font="Arial, 15", command=nivelt_al_ing10)

    # label com o nivel de turma do aluno 10 de ingles
    lbl_nivelt_al_ing10 = Label(janela_turma_ingles, text=nivelt, bg="white", font="Arial, 17")

    # posicionamento dos objetos do aluno 10
    add_al_ing10.place(x=20, y=500)
    lbl_nome_al_ing10.place(x=120, y=505)

    add_nota_ing10.place(x=600, y=500)
    lbl_nota_al_ing10.place(x=700, y=505)

    presenc_al_ing10.place(x=770, y=500)
    lbl_presenc_al_ing10.place(x=900, y=505)

    lbl_nome_nv_al_ing10.place(x=950, y=505)
    lbl_nv_al_ing10.place(x=1050, y=505)

    bt_nv_turma_al_ing10.place(x=1100, y=500)
    lbl_nivelt_al_ing10.place(x=1205, y=505)

    #####################################################################
    # fim da estrutura do aluno 10
    #####################################################################

    #####################################################################
    #####################################################################
    #####################################################################
    #####################################################################
    # barra de rolagem lateral direita
    sb = Scrollbar(janela_turma_ingles)
    sb.pack(side='right', fill=Y)
    janela_turma_ingles.mainloop()


#####################################################################
# parte do programa dedicada ao aluno 1 de ingles
#####################################################################

def nome_al_ing1():
    global nome_ing1, tela
    tela = Tk()
    tela.configure(bg="white")
    tela.geometry("775x100+50+100")
    tela.title("Entrada do nome do aluno")

    nome_ing1 = Entry(tela, width=50, font="Arial, 20")
    nome_ing1.place(x=10, y=25)

    bt_salva = Button(tela, text="Salvar", bg="blue", fg="white", font="Arial, 15", command=salvar_nome_ing1)
    bt_salva.place(x=600, y=60)

    tela.mainloop()


def salvar_nome_ing1():
    global nome_ing1, lbl_nome_al_ing1, tela
    nome = nome_ing1.get().title()
    tela.destroy()

    arquivo = open('bd_al_ing1.pck', 'rb')
    bd_al_ing1 = pickle.load(arquivo)
    arquivo.close()

    bd_al_ing1["nome"] = nome
    arquivo = open('bd_al_ing1.pck', 'wb')
    pickle.dump(bd_al_ing1, arquivo)
    arquivo.close()
    lbl_nome_al_ing1["text"] = nome


def nota_al_ing1():
    global nota_ing1, tela, lbl_msg_nota_al_ing1
    tela = Tk()
    tela.configure(bg="white")
    tela.geometry("775x100+50+100")
    tela.title("Entrada do nome do aluno")

    nota_ing1 = Entry(tela, width=50, font="Arial, 20")

    bt_salva = Button(tela, text="Salvar", bg="blue", fg="white", font="Arial, 15", command=salvar_nota_ing1)

    lbl_msg_nota_al_ing1 = Label(tela, text="Digite a nota do aluno(valor entre 0 e 10)", bg="green", fg="white",
                                 font="Arial, 15")

    nota_ing1.place(x=10, y=25)
    bt_salva.place(x=600, y=60)
    lbl_msg_nota_al_ing1.place(x=15, y=65)
    tela.mainloop()


def salvar_nota_ing1():
    global nota_ing1, lbl_nota_al_ing1, tela, lbl_nv_al_ing1, lbl_msg_nota_al_ing1
    note = int(nota_ing1.get())
    nota = nota_ing1.get()
    lbl = note // 2

    if note < 0 or note > 10:
        lbl_msg_nota_al_ing1["text"] = "ERRO! a nota do aluno deve ser um numero entre 0 e 10"
        lbl_msg_nota_al_ing1["bg"] = "red"
        raise Exception
    elif note >= 0 and note <= 10:
        tela.destroy()
        arquivo = open('bd_al_ing1.pck', 'rb')
        bd_al_ing1 = pickle.load(arquivo)
        arquivo.close()

        bd_al_ing1["nota"] = nota

        arquivo = open('bd_al_ing1.pck', 'wb')
        pickle.dump(bd_al_ing1, arquivo)
        arquivo.close()

        lbl_nota_al_ing1["text"] = str(nota)
        lbl_nv_al_ing1["text"] = str(lbl)


def presenc_al_ing1():
    global presenc_ing1, tela
    tela = Tk()
    tela.configure(bg="white")
    tela.geometry("775x100+50+100")
    tela.title("Entrada das presenças do aluno")

    presenc_ing1 = Entry(tela, width=50, font="Arial, 20")
    presenc_ing1.place(x=10, y=25)

    bt_salva = Button(tela, text="Salvar", bg="blue", fg="white", font="Arial, 15", command=salvar_presenc_ing1)
    bt_salva.place(x=600, y=60)

    tela.mainloop()


def salvar_presenc_ing1():
    global presenc_ing1, lbl_presenc_al_ing1, tela
    presenc = presenc_ing1.get()
    note = int(presenc_ing1.get())
    tela.destroy()

    arquivo = open('bd_al_ing1.pck', 'rb')
    bd_al_ing1 = pickle.load(arquivo)
    arquivo.close()

    bd_al_ing1["presenc"]=presenc

    arquivo = open('bd_al_ing1.pck', 'wb')
    lbl_presenc_al_ing1["text"] = presenc
    pickle.dump(bd_al_ing1, arquivo)
    arquivo.close()


def nivelt_al_ing1():
    global nivelt_ing1, tela
    tela = Tk()
    tela.configure(bg="white")
    tela.geometry("775x100+50+100")
    tela.title("Entrada do Nivel de Turma do Aluno do aluno")

    nivelt_ing1 = Entry(tela, width=50, font="Arial, 20")
    nivelt_ing1.place(x=10, y=25)

    bt_salva = Button(tela, text="Salvar", bg="blue", fg="white", font="Arial, 15", command=salvar_nivelt_ing1)
    bt_salva.place(x=600, y=60)

    tela.mainloop()


def salvar_nivelt_ing1():
    global nivelt_ing1, lbl_nivelt_al_ing1, tela
    nivelt = nivelt_ing1.get()
    tela.destroy()

    arquivo = open('bd_al_ing1.pck', 'rb')
    bd_al_ing1 = pickle.load(arquivo)
    arquivo.close()

    bd_al_ing1["nivelt"] = nivelt
    arquivo = open('bd_al_ing1.pck', 'wb')
    pickle.dump(bd_al_ing1, arquivo)
    arquivo.close()

    lbl_nivelt_al_ing1["text"]=nivelt

#####################################################################
# fim parte do programa dedicada ao aluno 1 de ingles
#####################################################################

#####################################################################
#####################################################################
#####################################################################



#####################################################################
# parte do programa dedicada ao aluno 2 de ingles
#####################################################################

def nome_al_ing2():
    global nome_ing2, tela
    tela = Tk()
    tela.configure(bg="white")
    tela.geometry("775x100+50+100")
    tela.title("Entrada do nome do aluno")

    nome_ing2 = Entry(tela, width=50, font="Arial, 20")
    nome_ing2.place(x=10, y=25)

    bt_salva = Button(tela, text="Salvar", bg="blue", fg="white", font="Arial, 15", command=salvar_nome_ing2)
    bt_salva.place(x=600, y=60)

    tela.mainloop()


def salvar_nome_ing2():
    global nome_ing2, lbl_nome_al_ing2, tela
    nome = nome_ing2.get().title()
    tela.destroy()

    arquivo = open('bd_al_ing2.pck', 'rb')
    bd_al_ing2 = pickle.load(arquivo)
    arquivo.close()

    bd_al_ing2["nome"] = nome
    arquivo = open('bd_al_ing2.pck', 'wb')
    pickle.dump(bd_al_ing2, arquivo)
    arquivo.close()
    lbl_nome_al_ing2["text"] = nome


def nota_al_ing2():
    global nota_ing2, tela, lbl_msg_nota_al_ing2
    tela = Tk()
    tela.configure(bg="white")
    tela.geometry("775x100+50+100")
    tela.title("Entrada do nome do aluno")

    nota_ing2 = Entry(tela, width=50, font="Arial, 20")

    bt_salva = Button(tela, text="Salvar", bg="blue", fg="white", font="Arial, 15", command=salvar_nota_ing2)

    lbl_msg_nota_al_ing2 = Label(tela, text="Digite a nota do aluno(valor entre 0 e 10)", bg="green", fg="white",
                                 font="Arial, 15")

    nota_ing2.place(x=10, y=25)
    bt_salva.place(x=600, y=60)
    lbl_msg_nota_al_ing2.place(x=15, y=65)
    tela.mainloop()


def salvar_nota_ing2():
    global nota_ing2, lbl_nota_al_ing2, tela, lbl_nv_al_ing2, lbl_msg_nota_al_ing2
    note = int(nota_ing2.get())
    nota = nota_ing2.get()
    lbl = note // 2

    if note < 0 or note > 10:
        lbl_msg_nota_al_ing2["text"] = "ERRO! a nota do aluno deve ser um numero entre 0 e 10"
        lbl_msg_nota_al_ing2["bg"] = "red"
        raise Exception
    elif note >= 0 and note <= 10:
        tela.destroy()
        arquivo = open('bd_al_ing2.pck', 'rb')
        bd_al_ing2 = pickle.load(arquivo)
        arquivo.close()

        bd_al_ing2["nota"] = nota

        arquivo = open('bd_al_ing2.pck', 'wb')
        pickle.dump(bd_al_ing2, arquivo)
        arquivo.close()

        lbl_nota_al_ing2["text"] = str(nota)
        lbl_nv_al_ing2["text"] = str(lbl)


def presenc_al_ing2():
    global presenc_ing2, tela
    tela = Tk()
    tela.configure(bg="white")
    tela.geometry("775x100+50+100")
    tela.title("Entrada das presenças do aluno")

    presenc_ing2 = Entry(tela, width=50, font="Arial, 20")
    presenc_ing2.place(x=10, y=25)

    bt_salva = Button(tela, text="Salvar", bg="blue", fg="white", font="Arial, 15", command=salvar_presenc_ing2)
    bt_salva.place(x=600, y=60)

    tela.mainloop()


def salvar_presenc_ing2():
    global presenc_ing2, lbl_presenc_al_ing2, tela
    presenc = presenc_ing2.get()
    note = int(presenc_ing2.get())
    tela.destroy()

    arquivo = open('bd_al_ing2.pck', 'rb')
    bd_al_ing2 = pickle.load(arquivo)
    arquivo.close()

    bd_al_ing2["presenc"]=presenc

    arquivo = open('bd_al_ing2.pck', 'wb')
    lbl_presenc_al_ing2["text"] = presenc
    pickle.dump(bd_al_ing2, arquivo)
    arquivo.close()


def nivelt_al_ing2():
    global nivelt_ing2, tela
    tela = Tk()
    tela.configure(bg="white")
    tela.geometry("775x100+50+100")
    tela.title("Entrada do Nivel de Turma do Aluno do aluno")

    nivelt_ing2 = Entry(tela, width=50, font="Arial, 20")
    nivelt_ing2.place(x=10, y=25)

    bt_salva = Button(tela, text="Salvar", bg="blue", fg="white", font="Arial, 15", command=salvar_nivelt_ing2)
    bt_salva.place(x=600, y=60)

    tela.mainloop()


def salvar_nivelt_ing2():
    global nivelt_ing2, lbl_nivelt_al_ing2, tela
    nivelt = nivelt_ing2.get()
    tela.destroy()

    arquivo = open('bd_al_ing2.pck', 'rb')
    bd_al_ing2 = pickle.load(arquivo)
    arquivo.close()

    bd_al_ing2["nivelt"] = nivelt
    arquivo = open('bd_al_ing2.pck', 'wb')
    pickle.dump(bd_al_ing2, arquivo)
    arquivo.close()

    lbl_nivelt_al_ing2["text"]=nivelt

#####################################################################
# fim parte do programa dedicada ao aluno 2 de ingles
#####################################################################

#####################################################################
#####################################################################
#####################################################################



#####################################################################
# parte do programa dedicada ao aluno 3 de ingles
#####################################################################

def nome_al_ing3():
    global nome_ing3, tela
    tela = Tk()
    tela.configure(bg="white")
    tela.geometry("775x100+50+100")
    tela.title("Entrada do nome do aluno")

    nome_ing3 = Entry(tela, width=50, font="Arial, 20")
    nome_ing3.place(x=10, y=25)

    bt_salva = Button(tela, text="Salvar", bg="blue", fg="white", font="Arial, 15", command=salvar_nome_ing3)
    bt_salva.place(x=600, y=60)

    tela.mainloop()


def salvar_nome_ing3():
    global nome_ing3, lbl_nome_al_ing3, tela
    nome = nome_ing3.get().title()
    tela.destroy()

    arquivo = open('bd_al_ing3.pck', 'rb')
    bd_al_ing3 = pickle.load(arquivo)
    arquivo.close()

    bd_al_ing3["nome"] = nome
    arquivo = open('bd_al_ing3.pck', 'wb')
    pickle.dump(bd_al_ing3, arquivo)
    arquivo.close()
    lbl_nome_al_ing3["text"] = nome


def nota_al_ing3():
    global nota_ing3, tela, lbl_msg_nota_al_ing3
    tela = Tk()
    tela.configure(bg="white")
    tela.geometry("775x100+50+100")
    tela.title("Entrada do nome do aluno")

    nota_ing3 = Entry(tela, width=50, font="Arial, 20")

    bt_salva = Button(tela, text="Salvar", bg="blue", fg="white", font="Arial, 15", command=salvar_nota_ing3)

    lbl_msg_nota_al_ing3 = Label(tela, text="Digite a nota do aluno(valor entre 0 e 10)", bg="green", fg="white",
                                 font="Arial, 15")

    nota_ing3.place(x=10, y=25)
    bt_salva.place(x=600, y=60)
    lbl_msg_nota_al_ing3.place(x=15, y=65)
    tela.mainloop()


def salvar_nota_ing3():
    global nota_ing3, lbl_nota_al_ing3, tela, lbl_nv_al_ing3, lbl_msg_nota_al_ing3
    note = int(nota_ing3.get())
    nota = nota_ing3.get()
    lbl = note // 2

    if note < 0 or note > 10:
        lbl_msg_nota_al_ing3["text"] = "ERRO! a nota do aluno deve ser um numero entre 0 e 10"
        lbl_msg_nota_al_ing3["bg"] = "red"
        raise Exception
    elif note >= 0 and note <= 10:
        tela.destroy()
        arquivo = open('bd_al_ing3.pck', 'rb')
        bd_al_ing3 = pickle.load(arquivo)
        arquivo.close()

        bd_al_ing3["nota"] = nota

        arquivo = open('bd_al_ing3.pck', 'wb')
        pickle.dump(bd_al_ing3, arquivo)
        arquivo.close()

        lbl_nota_al_ing3["text"] = str(nota)
        lbl_nv_al_ing3["text"] = str(lbl)


def presenc_al_ing3():
    global presenc_ing3, tela
    tela = Tk()
    tela.configure(bg="white")
    tela.geometry("775x100+50+100")
    tela.title("Entrada das presenças do aluno")

    presenc_ing3 = Entry(tela, width=50, font="Arial, 20")
    presenc_ing3.place(x=10, y=25)

    bt_salva = Button(tela, text="Salvar", bg="blue", fg="white", font="Arial, 15", command=salvar_presenc_ing3)
    bt_salva.place(x=600, y=60)

    tela.mainloop()


def salvar_presenc_ing3():
    global presenc_ing3, lbl_presenc_al_ing3, tela
    presenc = presenc_ing3.get()
    note = int(presenc_ing3.get())
    tela.destroy()

    arquivo = open('bd_al_ing3.pck', 'rb')
    bd_al_ing3 = pickle.load(arquivo)
    arquivo.close()

    bd_al_ing3["presenc"]=presenc

    arquivo = open('bd_al_ing3.pck', 'wb')
    lbl_presenc_al_ing3["text"] = presenc
    pickle.dump(bd_al_ing3, arquivo)
    arquivo.close()


def nivelt_al_ing3():
    global nivelt_ing3, tela
    tela = Tk()
    tela.configure(bg="white")
    tela.geometry("775x100+50+100")
    tela.title("Entrada do Nivel de Turma do Aluno do aluno")

    nivelt_ing3 = Entry(tela, width=50, font="Arial, 20")
    nivelt_ing3.place(x=10, y=25)

    bt_salva = Button(tela, text="Salvar", bg="blue", fg="white", font="Arial, 15", command=salvar_nivelt_ing3)
    bt_salva.place(x=600, y=60)

    tela.mainloop()


def salvar_nivelt_ing3():
    global nivelt_ing3, lbl_nivelt_al_ing3, tela
    nivelt = nivelt_ing3.get()
    tela.destroy()

    arquivo = open('bd_al_ing3.pck', 'rb')
    bd_al_ing3 = pickle.load(arquivo)
    arquivo.close()

    bd_al_ing3["nivelt"] = nivelt
    arquivo = open('bd_al_ing3.pck', 'wb')
    pickle.dump(bd_al_ing3, arquivo)
    arquivo.close()

    lbl_nivelt_al_ing3["text"]=nivelt

#####################################################################
# fim parte do programa dedicada ao aluno 3 de ingles
#####################################################################

#####################################################################
#####################################################################
#####################################################################



#####################################################################
# parte do programa dedicada ao aluno 4 de ingles
#####################################################################

def nome_al_ing4():
    global nome_ing4, tela
    tela = Tk()
    tela.configure(bg="white")
    tela.geometry("775x100+50+100")
    tela.title("Entrada do nome do aluno")

    nome_ing4 = Entry(tela, width=50, font="Arial, 20")
    nome_ing4.place(x=10, y=25)

    bt_salva = Button(tela, text="Salvar", bg="blue", fg="white", font="Arial, 15", command=salvar_nome_ing4)
    bt_salva.place(x=600, y=60)

    tela.mainloop()


def salvar_nome_ing4():
    global nome_ing4, lbl_nome_al_ing4, tela
    nome = nome_ing4.get().title()
    tela.destroy()

    arquivo = open('bd_al_ing4.pck', 'rb')
    bd_al_ing4 = pickle.load(arquivo)
    arquivo.close()

    bd_al_ing4["nome"] = nome
    arquivo = open('bd_al_ing4.pck', 'wb')
    pickle.dump(bd_al_ing4, arquivo)
    arquivo.close()
    lbl_nome_al_ing4["text"] = nome


def nota_al_ing4():
    global nota_ing4, tela, lbl_msg_nota_al_ing4
    tela = Tk()
    tela.configure(bg="white")
    tela.geometry("775x100+50+100")
    tela.title("Entrada do nome do aluno")

    nota_ing4 = Entry(tela, width=50, font="Arial, 20")

    bt_salva = Button(tela, text="Salvar", bg="blue", fg="white", font="Arial, 15", command=salvar_nota_ing4)

    lbl_msg_nota_al_ing4 = Label(tela, text="Digite a nota do aluno(valor entre 0 e 10)", bg="green", fg="white",
                                 font="Arial, 15")

    nota_ing4.place(x=10, y=25)
    bt_salva.place(x=600, y=60)
    lbl_msg_nota_al_ing4.place(x=15, y=65)
    tela.mainloop()


def salvar_nota_ing4():
    global nota_ing4, lbl_nota_al_ing4, tela, lbl_nv_al_ing4, lbl_msg_nota_al_ing4
    note = int(nota_ing4.get())
    nota = nota_ing4.get()
    lbl = note // 2

    if note < 0 or note > 10:
        lbl_msg_nota_al_ing4["text"] = "ERRO! a nota do aluno deve ser um numero entre 0 e 10"
        lbl_msg_nota_al_ing4["bg"] = "red"
        raise Exception
    elif note >= 0 and note <= 10:
        tela.destroy()
        arquivo = open('bd_al_ing4.pck', 'rb')
        bd_al_ing4 = pickle.load(arquivo)
        arquivo.close()

        bd_al_ing4["nota"] = nota

        arquivo = open('bd_al_ing4.pck', 'wb')
        pickle.dump(bd_al_ing4, arquivo)
        arquivo.close()

        lbl_nota_al_ing4["text"] = str(nota)
        lbl_nv_al_ing4["text"] = str(lbl)


def presenc_al_ing4():
    global presenc_ing4, tela
    tela = Tk()
    tela.configure(bg="white")
    tela.geometry("775x100+50+100")
    tela.title("Entrada das presenças do aluno")

    presenc_ing4 = Entry(tela, width=50, font="Arial, 20")
    presenc_ing4.place(x=10, y=25)

    bt_salva = Button(tela, text="Salvar", bg="blue", fg="white", font="Arial, 15", command=salvar_presenc_ing4)
    bt_salva.place(x=600, y=60)

    tela.mainloop()


def salvar_presenc_ing4():
    global presenc_ing4, lbl_presenc_al_ing4, tela
    presenc = presenc_ing4.get()
    note = int(presenc_ing4.get())
    tela.destroy()

    arquivo = open('bd_al_ing4.pck', 'rb')
    bd_al_ing4 = pickle.load(arquivo)
    arquivo.close()

    bd_al_ing4["presenc"]=presenc

    arquivo = open('bd_al_ing4.pck', 'wb')
    lbl_presenc_al_ing4["text"] = presenc
    pickle.dump(bd_al_ing4, arquivo)
    arquivo.close()


def nivelt_al_ing4():
    global nivelt_ing4, tela
    tela = Tk()
    tela.configure(bg="white")
    tela.geometry("775x100+50+100")
    tela.title("Entrada do Nivel de Turma do Aluno do aluno")

    nivelt_ing4 = Entry(tela, width=50, font="Arial, 20")
    nivelt_ing4.place(x=10, y=25)

    bt_salva = Button(tela, text="Salvar", bg="blue", fg="white", font="Arial, 15", command=salvar_nivelt_ing4)
    bt_salva.place(x=600, y=60)

    tela.mainloop()


def salvar_nivelt_ing4():
    global nivelt_ing4, lbl_nivelt_al_ing4, tela
    nivelt = nivelt_ing4.get()
    tela.destroy()

    arquivo = open('bd_al_ing4.pck', 'rb')
    bd_al_ing4 = pickle.load(arquivo)
    arquivo.close()

    bd_al_ing4["nivelt"] = nivelt
    arquivo = open('bd_al_ing4.pck', 'wb')
    pickle.dump(bd_al_ing4, arquivo)
    arquivo.close()

    lbl_nivelt_al_ing4["text"]=nivelt

#####################################################################
# fim parte do programa dedicada ao aluno 4 de ingles
#####################################################################

#####################################################################
#####################################################################
#####################################################################



#####################################################################
# parte do programa dedicada ao aluno 5 de ingles
#####################################################################

def nome_al_ing5():
    global nome_ing5, tela
    tela = Tk()
    tela.configure(bg="white")
    tela.geometry("775x100+50+100")
    tela.title("Entrada do nome do aluno")

    nome_ing5 = Entry(tela, width=50, font="Arial, 20")
    nome_ing5.place(x=10, y=25)

    bt_salva = Button(tela, text="Salvar", bg="blue", fg="white", font="Arial, 15", command=salvar_nome_ing5)
    bt_salva.place(x=600, y=60)

    tela.mainloop()


def salvar_nome_ing5():
    global nome_ing5, lbl_nome_al_ing5, tela
    nome = nome_ing5.get().title()
    tela.destroy()

    arquivo = open('bd_al_ing5.pck', 'rb')
    bd_al_ing5 = pickle.load(arquivo)
    arquivo.close()

    bd_al_ing5["nome"] = nome
    arquivo = open('bd_al_ing5.pck', 'wb')
    pickle.dump(bd_al_ing5, arquivo)
    arquivo.close()
    lbl_nome_al_ing5["text"] = nome


def nota_al_ing5():
    global nota_ing5, tela, lbl_msg_nota_al_ing5
    tela = Tk()
    tela.configure(bg="white")
    tela.geometry("775x100+50+100")
    tela.title("Entrada do nome do aluno")

    nota_ing5 = Entry(tela, width=50, font="Arial, 20")

    bt_salva = Button(tela, text="Salvar", bg="blue", fg="white", font="Arial, 15", command=salvar_nota_ing5)

    lbl_msg_nota_al_ing5 = Label(tela, text="Digite a nota do aluno(valor entre 0 e 10)", bg="green", fg="white",
                                 font="Arial, 15")

    nota_ing5.place(x=10, y=25)
    bt_salva.place(x=600, y=60)
    lbl_msg_nota_al_ing5.place(x=15, y=65)
    tela.mainloop()


def salvar_nota_ing5():
    global nota_ing5, lbl_nota_al_ing5, tela, lbl_nv_al_ing5, lbl_msg_nota_al_ing5
    note = int(nota_ing5.get())
    nota = nota_ing5.get()
    lbl = note // 2

    if note < 0 or note > 10:
        lbl_msg_nota_al_ing5["text"] = "ERRO! a nota do aluno deve ser um numero entre 0 e 10"
        lbl_msg_nota_al_ing5["bg"] = "red"
        raise Exception
    elif note >= 0 and note <= 10:
        tela.destroy()
        arquivo = open('bd_al_ing5.pck', 'rb')
        bd_al_ing5 = pickle.load(arquivo)
        arquivo.close()

        bd_al_ing5["nota"] = nota

        arquivo = open('bd_al_ing5.pck', 'wb')
        pickle.dump(bd_al_ing5, arquivo)
        arquivo.close()

        lbl_nota_al_ing5["text"] = str(nota)
        lbl_nv_al_ing5["text"] = str(lbl)


def presenc_al_ing5():
    global presenc_ing5, tela
    tela = Tk()
    tela.configure(bg="white")
    tela.geometry("775x100+50+100")
    tela.title("Entrada das presenças do aluno")

    presenc_ing5 = Entry(tela, width=50, font="Arial, 20")
    presenc_ing5.place(x=10, y=25)

    bt_salva = Button(tela, text="Salvar", bg="blue", fg="white", font="Arial, 15", command=salvar_presenc_ing5)
    bt_salva.place(x=600, y=60)

    tela.mainloop()


def salvar_presenc_ing5():
    global presenc_ing5, lbl_presenc_al_ing5, tela
    presenc = presenc_ing5.get()
    note = int(presenc_ing5.get())
    tela.destroy()

    arquivo = open('bd_al_ing5.pck', 'rb')
    bd_al_ing5 = pickle.load(arquivo)
    arquivo.close()

    bd_al_ing5["presenc"]=presenc

    arquivo = open('bd_al_ing5.pck', 'wb')
    lbl_presenc_al_ing5["text"] = presenc
    pickle.dump(bd_al_ing5, arquivo)
    arquivo.close()


def nivelt_al_ing5():
    global nivelt_ing5, tela
    tela = Tk()
    tela.configure(bg="white")
    tela.geometry("775x100+50+100")
    tela.title("Entrada do Nivel de Turma do Aluno do aluno")

    nivelt_ing5 = Entry(tela, width=50, font="Arial, 20")
    nivelt_ing5.place(x=10, y=25)

    bt_salva = Button(tela, text="Salvar", bg="blue", fg="white", font="Arial, 15", command=salvar_nivelt_ing5)
    bt_salva.place(x=600, y=60)

    tela.mainloop()


def salvar_nivelt_ing5():
    global nivelt_ing5, lbl_nivelt_al_ing5, tela
    nivelt = nivelt_ing5.get()
    tela.destroy()

    arquivo = open('bd_al_ing5.pck', 'rb')
    bd_al_ing5 = pickle.load(arquivo)
    arquivo.close()

    bd_al_ing5["nivelt"] = nivelt
    arquivo = open('bd_al_ing5.pck', 'wb')
    pickle.dump(bd_al_ing5, arquivo)
    arquivo.close()

    lbl_nivelt_al_ing5["text"]=nivelt

#####################################################################
# fim parte do programa dedicada ao aluno 5 de ingles
#####################################################################

#####################################################################
#####################################################################
#####################################################################



#####################################################################
# parte do programa dedicada ao aluno 6 de ingles
#####################################################################

def nome_al_ing6():
    global nome_ing6, tela
    tela = Tk()
    tela.configure(bg="white")
    tela.geometry("775x100+50+100")
    tela.title("Entrada do nome do aluno")

    nome_ing6 = Entry(tela, width=50, font="Arial, 20")
    nome_ing6.place(x=10, y=25)

    bt_salva = Button(tela, text="Salvar", bg="blue", fg="white", font="Arial, 15", command=salvar_nome_ing6)
    bt_salva.place(x=600, y=60)

    tela.mainloop()


def salvar_nome_ing6():
    global nome_ing6, lbl_nome_al_ing6, tela
    nome = nome_ing6.get().title()
    tela.destroy()

    arquivo = open('bd_al_ing6.pck', 'rb')
    bd_al_ing6 = pickle.load(arquivo)
    arquivo.close()

    bd_al_ing6["nome"] = nome
    arquivo = open('bd_al_ing6.pck', 'wb')
    pickle.dump(bd_al_ing6, arquivo)
    arquivo.close()
    lbl_nome_al_ing6["text"] = nome


def nota_al_ing6():
    global nota_ing6, tela, lbl_msg_nota_al_ing6
    tela = Tk()
    tela.configure(bg="white")
    tela.geometry("775x100+50+100")
    tela.title("Entrada do nome do aluno")

    nota_ing6 = Entry(tela, width=50, font="Arial, 20")

    bt_salva = Button(tela, text="Salvar", bg="blue", fg="white", font="Arial, 15", command=salvar_nota_ing6)

    lbl_msg_nota_al_ing6 = Label(tela, text="Digite a nota do aluno(valor entre 0 e 10)", bg="green", fg="white",
                                 font="Arial, 15")

    nota_ing6.place(x=10, y=25)
    bt_salva.place(x=600, y=60)
    lbl_msg_nota_al_ing6.place(x=15, y=65)
    tela.mainloop()


def salvar_nota_ing6():
    global nota_ing6, lbl_nota_al_ing6, tela, lbl_nv_al_ing6, lbl_msg_nota_al_ing6
    note = int(nota_ing6.get())
    nota = nota_ing6.get()
    lbl = note // 2

    if note < 0 or note > 10:
        lbl_msg_nota_al_ing6["text"] = "ERRO! a nota do aluno deve ser um numero entre 0 e 10"
        lbl_msg_nota_al_ing6["bg"] = "red"
        raise Exception
    elif note >= 0 and note <= 10:
        tela.destroy()
        arquivo = open('bd_al_ing6.pck', 'rb')
        bd_al_ing6 = pickle.load(arquivo)
        arquivo.close()

        bd_al_ing6["nota"] = nota

        arquivo = open('bd_al_ing6.pck', 'wb')
        pickle.dump(bd_al_ing6, arquivo)
        arquivo.close()

        lbl_nota_al_ing6["text"] = str(nota)
        lbl_nv_al_ing6["text"] = str(lbl)


def presenc_al_ing6():
    global presenc_ing6, tela
    tela = Tk()
    tela.configure(bg="white")
    tela.geometry("775x100+50+100")
    tela.title("Entrada das presenças do aluno")

    presenc_ing6 = Entry(tela, width=50, font="Arial, 20")
    presenc_ing6.place(x=10, y=25)

    bt_salva = Button(tela, text="Salvar", bg="blue", fg="white", font="Arial, 15", command=salvar_presenc_ing6)
    bt_salva.place(x=600, y=60)

    tela.mainloop()


def salvar_presenc_ing6():
    global presenc_ing6, lbl_presenc_al_ing6, tela
    presenc = presenc_ing6.get()
    note = int(presenc_ing6.get())
    tela.destroy()

    arquivo = open('bd_al_ing6.pck', 'rb')
    bd_al_ing6 = pickle.load(arquivo)
    arquivo.close()

    bd_al_ing6["presenc"]=presenc

    arquivo = open('bd_al_ing6.pck', 'wb')
    lbl_presenc_al_ing6["text"] = presenc
    pickle.dump(bd_al_ing6, arquivo)
    arquivo.close()


def nivelt_al_ing6():
    global nivelt_ing6, tela
    tela = Tk()
    tela.configure(bg="white")
    tela.geometry("775x100+50+100")
    tela.title("Entrada do Nivel de Turma do Aluno do aluno")

    nivelt_ing6 = Entry(tela, width=50, font="Arial, 20")
    nivelt_ing6.place(x=10, y=25)

    bt_salva = Button(tela, text="Salvar", bg="blue", fg="white", font="Arial, 15", command=salvar_nivelt_ing6)
    bt_salva.place(x=600, y=60)

    tela.mainloop()


def salvar_nivelt_ing6():
    global nivelt_ing6, lbl_nivelt_al_ing6, tela
    nivelt = nivelt_ing6.get()
    tela.destroy()

    arquivo = open('bd_al_ing6.pck', 'rb')
    bd_al_ing6 = pickle.load(arquivo)
    arquivo.close()

    bd_al_ing6["nivelt"] = nivelt
    arquivo = open('bd_al_ing6.pck', 'wb')
    pickle.dump(bd_al_ing6, arquivo)
    arquivo.close()

    lbl_nivelt_al_ing6["text"]=nivelt

#####################################################################
# fim parte do programa dedicada ao aluno 6 de ingles
#####################################################################

#####################################################################
#####################################################################
#####################################################################



#####################################################################
# parte do programa dedicada ao aluno 7 de ingles
#####################################################################

def nome_al_ing7():
    global nome_ing7, tela
    tela = Tk()
    tela.configure(bg="white")
    tela.geometry("775x100+50+100")
    tela.title("Entrada do nome do aluno")

    nome_ing7 = Entry(tela, width=50, font="Arial, 20")
    nome_ing7.place(x=10, y=25)

    bt_salva = Button(tela, text="Salvar", bg="blue", fg="white", font="Arial, 15", command=salvar_nome_ing7)
    bt_salva.place(x=600, y=60)

    tela.mainloop()


def salvar_nome_ing7():
    global nome_ing7, lbl_nome_al_ing7, tela
    nome = nome_ing7.get().title()
    tela.destroy()

    arquivo = open('bd_al_ing7.pck', 'rb')
    bd_al_ing7 = pickle.load(arquivo)
    arquivo.close()

    bd_al_ing7["nome"] = nome
    arquivo = open('bd_al_ing7.pck', 'wb')
    pickle.dump(bd_al_ing7, arquivo)
    arquivo.close()
    lbl_nome_al_ing7["text"] = nome


def nota_al_ing7():
    global nota_ing7, tela, lbl_msg_nota_al_ing7
    tela = Tk()
    tela.configure(bg="white")
    tela.geometry("775x100+50+100")
    tela.title("Entrada do nome do aluno")

    nota_ing7 = Entry(tela, width=50, font="Arial, 20")

    bt_salva = Button(tela, text="Salvar", bg="blue", fg="white", font="Arial, 15", command=salvar_nota_ing7)

    lbl_msg_nota_al_ing7 = Label(tela, text="Digite a nota do aluno(valor entre 0 e 10)", bg="green", fg="white",
                                 font="Arial, 15")

    nota_ing7.place(x=10, y=25)
    bt_salva.place(x=600, y=60)
    lbl_msg_nota_al_ing7.place(x=15, y=65)
    tela.mainloop()


def salvar_nota_ing7():
    global nota_ing7, lbl_nota_al_ing7, tela, lbl_nv_al_ing7, lbl_msg_nota_al_ing7
    note = int(nota_ing7.get())
    nota = nota_ing7.get()
    lbl = note // 2

    if note < 0 or note > 10:
        lbl_msg_nota_al_ing7["text"] = "ERRO! a nota do aluno deve ser um numero entre 0 e 10"
        lbl_msg_nota_al_ing7["bg"] = "red"
        raise Exception
    elif note >= 0 and note <= 10:
        tela.destroy()
        arquivo = open('bd_al_ing7.pck', 'rb')
        bd_al_ing7 = pickle.load(arquivo)
        arquivo.close()

        bd_al_ing7["nota"] = nota

        arquivo = open('bd_al_ing7.pck', 'wb')
        pickle.dump(bd_al_ing7, arquivo)
        arquivo.close()

        lbl_nota_al_ing7["text"] = str(nota)
        lbl_nv_al_ing7["text"] = str(lbl)


def presenc_al_ing7():
    global presenc_ing7, tela
    tela = Tk()
    tela.configure(bg="white")
    tela.geometry("775x100+50+100")
    tela.title("Entrada das presenças do aluno")

    presenc_ing7 = Entry(tela, width=50, font="Arial, 20")
    presenc_ing7.place(x=10, y=25)

    bt_salva = Button(tela, text="Salvar", bg="blue", fg="white", font="Arial, 15", command=salvar_presenc_ing7)
    bt_salva.place(x=600, y=60)

    tela.mainloop()


def salvar_presenc_ing7():
    global presenc_ing7, lbl_presenc_al_ing7, tela
    presenc = presenc_ing7.get()
    note = int(presenc_ing7.get())
    tela.destroy()

    arquivo = open('bd_al_ing7.pck', 'rb')
    bd_al_ing7 = pickle.load(arquivo)
    arquivo.close()

    bd_al_ing7["presenc"]=presenc

    arquivo = open('bd_al_ing7.pck', 'wb')
    lbl_presenc_al_ing7["text"] = presenc
    pickle.dump(bd_al_ing7, arquivo)
    arquivo.close()


def nivelt_al_ing7():
    global nivelt_ing7, tela
    tela = Tk()
    tela.configure(bg="white")
    tela.geometry("775x100+50+100")
    tela.title("Entrada do Nivel de Turma do Aluno do aluno")

    nivelt_ing7 = Entry(tela, width=50, font="Arial, 20")
    nivelt_ing7.place(x=10, y=25)

    bt_salva = Button(tela, text="Salvar", bg="blue", fg="white", font="Arial, 15", command=salvar_nivelt_ing7)
    bt_salva.place(x=600, y=60)

    tela.mainloop()


def salvar_nivelt_ing7():
    global nivelt_ing7, lbl_nivelt_al_ing7, tela
    nivelt = nivelt_ing7.get()
    tela.destroy()

    arquivo = open('bd_al_ing7.pck', 'rb')
    bd_al_ing7 = pickle.load(arquivo)
    arquivo.close()

    bd_al_ing7["nivelt"] = nivelt
    arquivo = open('bd_al_ing7.pck', 'wb')
    pickle.dump(bd_al_ing7, arquivo)
    arquivo.close()

    lbl_nivelt_al_ing7["text"]=nivelt

#####################################################################
# fim parte do programa dedicada ao aluno 7 de ingles
#####################################################################

#####################################################################
#####################################################################
#####################################################################



#####################################################################
# parte do programa dedicada ao aluno 8 de ingles
#####################################################################

def nome_al_ing8():
    global nome_ing8, tela
    tela = Tk()
    tela.configure(bg="white")
    tela.geometry("775x100+50+100")
    tela.title("Entrada do nome do aluno")

    nome_ing8 = Entry(tela, width=50, font="Arial, 20")
    nome_ing8.place(x=10, y=25)

    bt_salva = Button(tela, text="Salvar", bg="blue", fg="white", font="Arial, 15", command=salvar_nome_ing8)
    bt_salva.place(x=600, y=60)

    tela.mainloop()


def salvar_nome_ing8():
    global nome_ing8, lbl_nome_al_ing8, tela
    nome = nome_ing8.get().title()
    tela.destroy()

    arquivo = open('bd_al_ing8.pck', 'rb')
    bd_al_ing8 = pickle.load(arquivo)
    arquivo.close()

    bd_al_ing8["nome"] = nome
    arquivo = open('bd_al_ing8.pck', 'wb')
    pickle.dump(bd_al_ing8, arquivo)
    arquivo.close()
    lbl_nome_al_ing8["text"] = nome


def nota_al_ing8():
    global nota_ing8, tela, lbl_msg_nota_al_ing8
    tela = Tk()
    tela.configure(bg="white")
    tela.geometry("775x100+50+100")
    tela.title("Entrada do nome do aluno")

    nota_ing8 = Entry(tela, width=50, font="Arial, 20")

    bt_salva = Button(tela, text="Salvar", bg="blue", fg="white", font="Arial, 15", command=salvar_nota_ing8)

    lbl_msg_nota_al_ing8 = Label(tela, text="Digite a nota do aluno(valor entre 0 e 10)", bg="green", fg="white",
                                 font="Arial, 15")

    nota_ing8.place(x=10, y=25)
    bt_salva.place(x=600, y=60)
    lbl_msg_nota_al_ing8.place(x=15, y=65)
    tela.mainloop()


def salvar_nota_ing8():
    global nota_ing8, lbl_nota_al_ing8, tela, lbl_nv_al_ing8, lbl_msg_nota_al_ing8
    note = int(nota_ing8.get())
    nota = nota_ing8.get()
    lbl = note // 2

    if note < 0 or note > 10:
        lbl_msg_nota_al_ing8["text"] = "ERRO! a nota do aluno deve ser um numero entre 0 e 10"
        lbl_msg_nota_al_ing8["bg"] = "red"
        raise Exception
    elif note >= 0 and note <= 10:
        tela.destroy()
        arquivo = open('bd_al_ing8.pck', 'rb')
        bd_al_ing8 = pickle.load(arquivo)
        arquivo.close()

        bd_al_ing8["nota"] = nota

        arquivo = open('bd_al_ing8.pck', 'wb')
        pickle.dump(bd_al_ing8, arquivo)
        arquivo.close()

        lbl_nota_al_ing8["text"] = str(nota)
        lbl_nv_al_ing8["text"] = str(lbl)


def presenc_al_ing8():
    global presenc_ing8, tela
    tela = Tk()
    tela.configure(bg="white")
    tela.geometry("775x100+50+100")
    tela.title("Entrada das presenças do aluno")

    presenc_ing8 = Entry(tela, width=50, font="Arial, 20")
    presenc_ing8.place(x=10, y=25)

    bt_salva = Button(tela, text="Salvar", bg="blue", fg="white", font="Arial, 15", command=salvar_presenc_ing8)
    bt_salva.place(x=600, y=60)

    tela.mainloop()


def salvar_presenc_ing8():
    global presenc_ing8, lbl_presenc_al_ing8, tela
    presenc = presenc_ing8.get()
    note = int(presenc_ing8.get())
    tela.destroy()

    arquivo = open('bd_al_ing8.pck', 'rb')
    bd_al_ing8 = pickle.load(arquivo)
    arquivo.close()

    bd_al_ing8["presenc"]=presenc

    arquivo = open('bd_al_ing8.pck', 'wb')
    lbl_presenc_al_ing8["text"] = presenc
    pickle.dump(bd_al_ing8, arquivo)
    arquivo.close()


def nivelt_al_ing8():
    global nivelt_ing8, tela
    tela = Tk()
    tela.configure(bg="white")
    tela.geometry("775x100+50+100")
    tela.title("Entrada do Nivel de Turma do Aluno do aluno")

    nivelt_ing8 = Entry(tela, width=50, font="Arial, 20")
    nivelt_ing8.place(x=10, y=25)

    bt_salva = Button(tela, text="Salvar", bg="blue", fg="white", font="Arial, 15", command=salvar_nivelt_ing8)
    bt_salva.place(x=600, y=60)

    tela.mainloop()


def salvar_nivelt_ing8():
    global nivelt_ing8, lbl_nivelt_al_ing8, tela
    nivelt = nivelt_ing8.get()
    tela.destroy()

    arquivo = open('bd_al_ing8.pck', 'rb')
    bd_al_ing8 = pickle.load(arquivo)
    arquivo.close()

    bd_al_ing8["nivelt"] = nivelt
    arquivo = open('bd_al_ing8.pck', 'wb')
    pickle.dump(bd_al_ing8, arquivo)
    arquivo.close()

    lbl_nivelt_al_ing8["text"]=nivelt

#####################################################################
# fim parte do programa dedicada ao aluno 8 de ingles
#####################################################################

#####################################################################
#####################################################################
#####################################################################



#####################################################################
# parte do programa dedicada ao aluno 9 de ingles
#####################################################################

def nome_al_ing9():
    global nome_ing9, tela
    tela = Tk()
    tela.configure(bg="white")
    tela.geometry("775x100+50+100")
    tela.title("Entrada do nome do aluno")

    nome_ing9 = Entry(tela, width=50, font="Arial, 20")
    nome_ing9.place(x=10, y=25)

    bt_salva = Button(tela, text="Salvar", bg="blue", fg="white", font="Arial, 15", command=salvar_nome_ing9)
    bt_salva.place(x=600, y=60)

    tela.mainloop()


def salvar_nome_ing9():
    global nome_ing9, lbl_nome_al_ing9, tela
    nome = nome_ing9.get().title()
    tela.destroy()

    arquivo = open('bd_al_ing9.pck', 'rb')
    bd_al_ing9 = pickle.load(arquivo)
    arquivo.close()

    bd_al_ing9["nome"] = nome
    arquivo = open('bd_al_ing9.pck', 'wb')
    pickle.dump(bd_al_ing9, arquivo)
    arquivo.close()
    lbl_nome_al_ing9["text"] = nome


def nota_al_ing9():
    global nota_ing9, tela, lbl_msg_nota_al_ing9
    tela = Tk()
    tela.configure(bg="white")
    tela.geometry("775x100+50+100")
    tela.title("Entrada do nome do aluno")

    nota_ing9 = Entry(tela, width=50, font="Arial, 20")

    bt_salva = Button(tela, text="Salvar", bg="blue", fg="white", font="Arial, 15", command=salvar_nota_ing9)

    lbl_msg_nota_al_ing9 = Label(tela, text="Digite a nota do aluno(valor entre 0 e 10)", bg="green", fg="white",
                                 font="Arial, 15")

    nota_ing9.place(x=10, y=25)
    bt_salva.place(x=600, y=60)
    lbl_msg_nota_al_ing9.place(x=15, y=65)
    tela.mainloop()


def salvar_nota_ing9():
    global nota_ing9, lbl_nota_al_ing9, tela, lbl_nv_al_ing9, lbl_msg_nota_al_ing9
    note = int(nota_ing9.get())
    nota = nota_ing9.get()
    lbl = note // 2

    if note < 0 or note > 10:
        lbl_msg_nota_al_ing9["text"] = "ERRO! a nota do aluno deve ser um numero entre 0 e 10"
        lbl_msg_nota_al_ing9["bg"] = "red"
        raise Exception
    elif note >= 0 and note <= 10:
        tela.destroy()
        arquivo = open('bd_al_ing9.pck', 'rb')
        bd_al_ing9 = pickle.load(arquivo)
        arquivo.close()

        bd_al_ing9["nota"] = nota

        arquivo = open('bd_al_ing9.pck', 'wb')
        pickle.dump(bd_al_ing9, arquivo)
        arquivo.close()

        lbl_nota_al_ing9["text"] = str(nota)
        lbl_nv_al_ing9["text"] = str(lbl)


def presenc_al_ing9():
    global presenc_ing9, tela
    tela = Tk()
    tela.configure(bg="white")
    tela.geometry("775x100+50+100")
    tela.title("Entrada das presenças do aluno")

    presenc_ing9 = Entry(tela, width=50, font="Arial, 20")
    presenc_ing9.place(x=10, y=25)

    bt_salva = Button(tela, text="Salvar", bg="blue", fg="white", font="Arial, 15", command=salvar_presenc_ing9)
    bt_salva.place(x=600, y=60)

    tela.mainloop()


def salvar_presenc_ing9():
    global presenc_ing9, lbl_presenc_al_ing9, tela
    presenc = presenc_ing9.get()
    note = int(presenc_ing9.get())
    tela.destroy()

    arquivo = open('bd_al_ing9.pck', 'rb')
    bd_al_ing9 = pickle.load(arquivo)
    arquivo.close()

    bd_al_ing9["presenc"]=presenc

    arquivo = open('bd_al_ing9.pck', 'wb')
    lbl_presenc_al_ing9["text"] = presenc
    pickle.dump(bd_al_ing9, arquivo)
    arquivo.close()


def nivelt_al_ing9():
    global nivelt_ing9, tela
    tela = Tk()
    tela.configure(bg="white")
    tela.geometry("775x100+50+100")
    tela.title("Entrada do Nivel de Turma do Aluno do aluno")

    nivelt_ing9 = Entry(tela, width=50, font="Arial, 20")
    nivelt_ing9.place(x=10, y=25)

    bt_salva = Button(tela, text="Salvar", bg="blue", fg="white", font="Arial, 15", command=salvar_nivelt_ing9)
    bt_salva.place(x=600, y=60)

    tela.mainloop()


def salvar_nivelt_ing9():
    global nivelt_ing9, lbl_nivelt_al_ing9, tela
    nivelt = nivelt_ing9.get()
    tela.destroy()

    arquivo = open('bd_al_ing9.pck', 'rb')
    bd_al_ing9 = pickle.load(arquivo)
    arquivo.close()

    bd_al_ing9["nivelt"] = nivelt
    arquivo = open('bd_al_ing9.pck', 'wb')
    pickle.dump(bd_al_ing9, arquivo)
    arquivo.close()

    lbl_nivelt_al_ing9["text"]=nivelt

#####################################################################
# fim parte do programa dedicada ao aluno 9 de ingles
#####################################################################

#####################################################################
#####################################################################
#####################################################################



#####################################################################
# parte do programa dedicada ao aluno 10 de ingles
#####################################################################

def nome_al_ing10():
    global nome_ing10, tela
    tela = Tk()
    tela.configure(bg="white")
    tela.geometry("775x100+50+100")
    tela.title("Entrada do nome do aluno")

    nome_ing10 = Entry(tela, width=50, font="Arial, 20")
    nome_ing10.place(x=10, y=25)

    bt_salva = Button(tela, text="Salvar", bg="blue", fg="white", font="Arial, 15", command=salvar_nome_ing10)
    bt_salva.place(x=600, y=60)

    tela.mainloop()


def salvar_nome_ing10():
    global nome_ing10, lbl_nome_al_ing10, tela
    nome = nome_ing10.get().title()
    lbl_nome_al_ing10["text"] = nome
    tela.destroy()

    arquivo = open('bd_al_ing10.pck', 'rb')
    bd_al_ing10 = pickle.load(arquivo)
    arquivo.close()

    bd_al_ing10["nome"] = nome
    arquivo = open('bd_al_ing10.pck', 'wb')
    pickle.dump(bd_al_ing10, arquivo)
    arquivo.close()


def nota_al_ing10():
    global nota_ing10, tela, lbl_msg_nota_al_ing10
    tela = Tk()
    tela.configure(bg="white")
    tela.geometry("775x100+50+100")
    tela.title("Entrada do nome do aluno")

    nota_ing10 = Entry(tela, width=50, font="Arial, 20")

    bt_salva = Button(tela, text="Salvar", bg="blue", fg="white", font="Arial, 15", command=salvar_nota_ing10)

    lbl_msg_nota_al_ing10 = Label(tela, text="Digite a nota do aluno(valor entre 0 e 10)", bg="green", fg="white",
                                 font="Arial, 15")

    nota_ing10.place(x=10, y=25)
    bt_salva.place(x=600, y=60)
    lbl_msg_nota_al_ing10.place(x=15, y=65)
    tela.mainloop()


def salvar_nota_ing10():
    global nota_ing10, lbl_nota_al_ing10, tela, lbl_nv_al_ing10, lbl_msg_nota_al_ing10
    note = int(nota_ing10.get())
    nota = nota_ing10.get()
    lbl = note // 2

    if note < 0 or note > 10:
        lbl_msg_nota_al_ing10["text"] = "ERRO! a nota do aluno deve ser um numero entre 0 e 10"
        lbl_msg_nota_al_ing10["bg"] = "red"
        raise Exception
    elif note >= 0 and note <= 10:
        tela.destroy()
        arquivo = open('bd_al_ing10.pck', 'rb')
        bd_al_ing10 = pickle.load(arquivo)
        arquivo.close()

        bd_al_ing10["nota"] = nota

        arquivo = open('bd_al_ing10.pck', 'wb')
        pickle.dump(bd_al_ing10, arquivo)
        arquivo.close()

        lbl_nota_al_ing10["text"] = str(nota)
        lbl_nv_al_ing10["text"] = str(lbl)


def presenc_al_ing10():
    global presenc_ing10, tela
    tela = Tk()
    tela.configure(bg="white")
    tela.geometry("775x100+50+100")
    tela.title("Entrada das presenças do aluno")

    presenc_ing10 = Entry(tela, width=50, font="Arial, 20")
    presenc_ing10.place(x=10, y=25)

    bt_salva = Button(tela, text="Salvar", bg="blue", fg="white", font="Arial, 15", command=salvar_presenc_ing10)
    bt_salva.place(x=600, y=60)

    tela.mainloop()


def salvar_presenc_ing10():
    global presenc_ing10, lbl_presenc_al_ing10, tela
    presenc = presenc_ing10.get()
    note = int(presenc_ing10.get())
    tela.destroy()

    arquivo = open('bd_al_ing10.pck', 'rb')
    bd_al_ing10 = pickle.load(arquivo)
    arquivo.close()

    bd_al_ing10["presenc"]=presenc

    arquivo = open('bd_al_ing10.pck', 'wb')
    lbl_presenc_al_ing10["text"] = presenc
    pickle.dump(bd_al_ing10, arquivo)
    arquivo.close()


def nivelt_al_ing10():
    global nivelt_ing10, tela
    tela = Tk()
    tela.configure(bg="white")
    tela.geometry("775x100+50+100")
    tela.title("Entrada do Nivel de Turma do Aluno do aluno")

    nivelt_ing10 = Entry(tela, width=50, font="Arial, 20")
    nivelt_ing10.place(x=10, y=25)

    bt_salva = Button(tela, text="Salvar", bg="blue", fg="white", font="Arial, 15", command=salvar_nivelt_ing10)
    bt_salva.place(x=600, y=60)

    tela.mainloop()


def salvar_nivelt_ing10():
    global nivelt_ing10, lbl_nivelt_al_ing10, tela
    nivelt = nivelt_ing10.get()
    tela.destroy()

    arquivo = open('bd_al_ing10.pck', 'rb')
    bd_al_ing10 = pickle.load(arquivo)
    arquivo.close()

    bd_al_ing10["nivelt"] = nivelt
    arquivo = open('bd_al_ing10.pck', 'wb')
    pickle.dump(bd_al_ing10, arquivo)
    arquivo.close()

    lbl_nivelt_al_ing10["text"]=nivelt

#####################################################################
# fim parte do programa dedicada ao aluno 10 de ingles
#####################################################################

#####################################################################
#####################################################################
#####################################################################



################################################################


def turma_espanhol():
    """tela para escolha dos alunos de espanhol"""
    global janela_escolha_de_turma,janela_turma_espanhol
    janela_escolha_de_turma.destroy()
    ################################################################
    global lbl_nv_al_esp1, lbl_nivelt_al_esp1, lbl_nome_al_esp1, janela_turma_espanhol, lbl_nota_al_esp1, presenc_al_esp1, lbl_presenc_al_esp1
    global lbl_nv_al_esp2, lbl_nivelt_al_esp2, lbl_nome_al_esp2, janela_turma_espanhol, lbl_nota_al_esp2, presenc_al_esp2, lbl_presenc_al_esp2
    global lbl_nv_al_esp3, lbl_nivelt_al_esp3, lbl_nome_al_esp3, janela_turma_espanhol, lbl_nota_al_esp3, presenc_al_esp3, lbl_presenc_al_esp3
    global lbl_nv_al_esp4, lbl_nivelt_al_esp4, lbl_nome_al_esp4, janela_turma_espanhol, lbl_nota_al_esp4, presenc_al_esp4, lbl_presenc_al_esp4
    global lbl_nv_al_esp5, lbl_nivelt_al_esp5, lbl_nome_al_esp5, janela_turma_espanhol, lbl_nota_al_esp5, presenc_al_esp5, lbl_presenc_al_esp5
    global lbl_nv_al_esp6, lbl_nivelt_al_esp6, lbl_nome_al_esp6, janela_turma_espanhol, lbl_nota_al_esp6, presenc_al_esp6, lbl_presenc_al_esp6
    global lbl_nv_al_esp7, lbl_nivelt_al_esp7, lbl_nome_al_esp7, janela_turma_espanhol, lbl_nota_al_esp7, presenc_al_esp7, lbl_presenc_al_esp7
    global lbl_nv_al_esp8, lbl_nivelt_al_esp8, lbl_nome_al_esp8, janela_turma_espanhol, lbl_nota_al_esp8, presenc_al_esp8, lbl_presenc_al_esp8
    global lbl_nv_al_esp9, lbl_nivelt_al_esp9, lbl_nome_al_esp9, janela_turma_espanhol, lbl_nota_al_esp9, presenc_al_esp9, lbl_presenc_al_esp9
    global lbl_nv_al_esp10, lbl_nivelt_al_esp10, lbl_nome_al_esp10, janela_turma_espanhol, lbl_nota_al_esp10, presenc_al_esp10, lbl_presenc_al_esp10

    ################################################################

    janela_turma_espanhol = Tk()
    janela_turma_espanhol.title("Mw Control - Turma de espanhol")
    janela_turma_espanhol.configure(bg="#c6ffc9")
    janela_turma_espanhol.geometry("1280x600+50+100")

    # botão de voltar pra tela anterior
    voltar = Button(janela_turma_espanhol, text="Voltar <-- ", width=7, bg="red", fg="white",
                    font=('Arial', '13', 'bold'), command=escolha_turmas3)
    voltar.place(x=20, y=0)

    # estrutura dedicada ao aluno 1 de espanhol
    #####################################################################
    # botão que muda o nome do aluno 1 de espanhol
    add_al_esp1 = Button(janela_turma_espanhol, bg="green", fg="white", width=6, height=1, text="Aluno 1:",
                         font="Arial, 15", command=nome_al_esp1)

    # ve o label nome do aluno 1 de espanhol no banco de dados

    arquivo = open('bd_al_esp1.pck', 'rb')
    bd_al_esp1 = pickle.load(arquivo)

    txt_nome_al_esp1 = bd_al_esp1["nome"]
    txt_nota_al_esp1 = bd_al_esp1["nota"]
    txt_presenc_al_esp1 = bd_al_esp1["presenc"]
    nivelt = bd_al_esp1["nivelt"]
    nv_al_esp1 = int(bd_al_esp1["nota"]) // 2
    arquivo.close()

    # label com o nome do aluno 1 de espanhol
    lbl_nome_al_esp1 = Label(janela_turma_espanhol, text=txt_nome_al_esp1, bg="white", font="Arial, 15")

    # botão que muda a nota do aluno 1 de espanhol
    add_nota_esp1 = Button(janela_turma_espanhol, bg="green", fg="white", width=6, height=1, text="Nota: ",
                           font="Arial, 15", command=nota_al_esp1)

    # label com a nota do aluno 1 de espanhol
    lbl_nota_al_esp1 = Label(janela_turma_espanhol, text=txt_nota_al_esp1, bg="white", font="Arial, 15")

    # botão que muda a presença do aluno 1 de espanhol
    presenc_al_esp1 = Button(janela_turma_espanhol, bg="green", fg="white", width=8, height=1, text="Presenças: ",
                             font="Arial, 15", command=presenc_al_esp1)

    # label com a presença do aluno 1 de espanhol
    lbl_presenc_al_esp1 = Label(janela_turma_espanhol, text=txt_presenc_al_esp1, bg="white", font="Arial, 15")

    # label com o nome nivel do aluno 1 de espanhol
    lbl_nome_nv_al_esp1 = Label(janela_turma_espanhol, text="Nivel:", width=6, bg="green", fg="white", font="Arial, 17")

    # label com o  nivel do aluno 1 de espanhol
    lbl_nv_al_esp1 = Label(janela_turma_espanhol, text=nv_al_esp1, bg="white", font="Arial, 17")

    # botão que muda o nome nivel de turma do aluno 1 de espanhol
    bt_nv_turma_al_esp1 = Button(janela_turma_espanhol, bg="green", fg="white", width=6, height=1, text="Nivel T: ",
                                 font="Arial, 15", command=nivelt_al_esp1)

    # label com o nivel de turma do aluno 1 de espanhol
    lbl_nivelt_al_esp1 = Label(janela_turma_espanhol, text=nivelt, bg="white", font="Arial, 17")

    # posicionamento dos objetos do aluno 1
    add_al_esp1.place(x=20, y=40)
    lbl_nome_al_esp1.place(x=120, y=45)

    add_nota_esp1.place(x=600, y=40)
    lbl_nota_al_esp1.place(x=700, y=45)

    presenc_al_esp1.place(x=770, y=40)
    lbl_presenc_al_esp1.place(x=900, y=45)

    lbl_nome_nv_al_esp1.place(x=950, y=45)
    lbl_nv_al_esp1.place(x=1050, y=45)

    bt_nv_turma_al_esp1.place(x=1100, y=40)
    lbl_nivelt_al_esp1.place(x=1205, y=45)

    #####################################################################
    # fim da estrutura do aluno 1
    #####################################################################

    #####################################################################
    #####################################################################
    #####################################################################

    # estrutura dedicada ao aluno 2 de espanhol
    #####################################################################
    # botão que muda o nome do aluno 2 de espanhol
    add_al_esp2 = Button(janela_turma_espanhol, bg="green", fg="white", width=6, height=1, text="aluno 2:",
                         font="Arial, 15", command=nome_al_esp2)

    # ve o label nome do aluno 2 de espanhol no banco de dados

    arquivo = open('bd_al_esp2.pck', 'rb')
    bd_al_esp2 = pickle.load(arquivo)

    txt_nome_al_esp2 = bd_al_esp2["nome"]
    txt_nota_al_esp2 = bd_al_esp2["nota"]
    txt_presenc_al_esp2 = bd_al_esp2["presenc"]
    nivelt = bd_al_esp2["nivelt"]
    nv_al_esp2 = int(bd_al_esp2["nota"]) // 2
    arquivo.close()

    # label com o nome do aluno 2 de espanhol
    lbl_nome_al_esp2 = Label(janela_turma_espanhol, text=txt_nome_al_esp2, bg="white", font="Arial, 15")

    # botão que muda a nota do aluno 2 de espanhol
    add_nota_esp2 = Button(janela_turma_espanhol, bg="green", fg="white", width=6, height=1, text="Nota: ",
                           font="Arial, 15", command=nota_al_esp2)

    # label com a nota do aluno 2 de espanhol
    lbl_nota_al_esp2 = Label(janela_turma_espanhol, text=txt_nota_al_esp2, bg="white", font="Arial, 15")

    # botão que muda a presença do aluno 2 de espanhol
    presenc_al_esp2 = Button(janela_turma_espanhol, bg="green", fg="white", width=8, height=1, text="Presenças: ",
                             font="Arial, 15", command=presenc_al_esp2)

    # label com a presença do aluno 2 de espanhol
    lbl_presenc_al_esp2 = Label(janela_turma_espanhol, text=txt_presenc_al_esp2, bg="white", font="Arial, 15")

    # label com o nome nivel do aluno 2 de espanhol
    lbl_nome_nv_al_esp2 = Label(janela_turma_espanhol, text="Nivel:", width=6, bg="green", fg="white", font="Arial, 17")

    # label com o  nivel do aluno 2 de espanhol
    lbl_nv_al_esp2 = Label(janela_turma_espanhol, text=nv_al_esp2, bg="white", font="Arial, 17")

    # botão que muda o nome nivel de turma do aluno 2 de espanhol
    bt_nv_turma_al_esp2 = Button(janela_turma_espanhol, bg="green", fg="white", width=6, height=1, text="Nivel T: ",
                                 font="Arial, 15", command=nivelt_al_esp2)

    # label com o nivel de turma do aluno 2 de espanhol
    lbl_nivelt_al_esp2 = Label(janela_turma_espanhol, text=nivelt, bg="white", font="Arial, 17")

    # posicionamento dos objetos do aluno 2
    add_al_esp2.place(x=20, y=90)
    lbl_nome_al_esp2.place(x=120, y=95)

    add_nota_esp2.place(x=600, y=90)
    lbl_nota_al_esp2.place(x=700, y=95)

    presenc_al_esp2.place(x=770, y=90)
    lbl_presenc_al_esp2.place(x=900, y=95)

    lbl_nome_nv_al_esp2.place(x=950, y=95)
    lbl_nv_al_esp2.place(x=1050, y=95)

    bt_nv_turma_al_esp2.place(x=1100, y=90)
    lbl_nivelt_al_esp2.place(x=1205, y=95)
    #####################################################################
    # fim da estrutura do aluno 2
    #####################################################################

    #####################################################################
    #####################################################################
    #####################################################################

    # estrutura dedicada ao aluno 3 de espanhol
    #####################################################################
    # botão que muda o nome do aluno 3 de espanhol
    add_al_esp3 = Button(janela_turma_espanhol, bg="green", fg="white", width=6, height=1, text="aluno 3:",
                         font="Arial, 15", command=nome_al_esp3)

    # ve o label nome do aluno 3 de espanhol no banco de dados

    arquivo = open('bd_al_esp3.pck', 'rb')
    bd_al_esp3 = pickle.load(arquivo)

    txt_nome_al_esp3 = bd_al_esp3["nome"]
    txt_nota_al_esp3 = bd_al_esp3["nota"]
    txt_presenc_al_esp3 = bd_al_esp3["presenc"]
    nivelt = bd_al_esp3["nivelt"]
    nv_al_esp3 = int(bd_al_esp3["nota"]) // 2
    arquivo.close()

    # label com o nome do aluno 3 de espanhol
    lbl_nome_al_esp3 = Label(janela_turma_espanhol, text=txt_nome_al_esp3, bg="white", font="Arial, 15")

    # botão que muda a nota do aluno 3 de espanhol
    add_nota_esp3 = Button(janela_turma_espanhol, bg="green", fg="white", width=6, height=1, text="Nota: ",
                           font="Arial, 15", command=nota_al_esp3)

    # label com a nota do aluno 3 de espanhol
    lbl_nota_al_esp3 = Label(janela_turma_espanhol, text=txt_nota_al_esp3, bg="white", font="Arial, 15")

    # botão que muda a presença do aluno 3 de espanhol
    presenc_al_esp3 = Button(janela_turma_espanhol, bg="green", fg="white", width=8, height=1, text="Presenças: ",
                             font="Arial, 15", command=presenc_al_esp3)

    # label com a presença do aluno 3 de espanhol
    lbl_presenc_al_esp3 = Label(janela_turma_espanhol, text=txt_presenc_al_esp3, bg="white", font="Arial, 15")

    # label com o nome nivel do aluno 3 de espanhol
    lbl_nome_nv_al_esp3 = Label(janela_turma_espanhol, text="Nivel:", width=6, bg="green", fg="white", font="Arial, 17")

    # label com o  nivel do aluno 3 de espanhol
    lbl_nv_al_esp3 = Label(janela_turma_espanhol, text=nv_al_esp3, bg="white", font="Arial, 17")

    # botão que muda o nome nivel de turma do aluno 3 de espanhol
    bt_nv_turma_al_esp3 = Button(janela_turma_espanhol, bg="green", fg="white", width=6, height=1, text="Nivel T: ",
                                 font="Arial, 15", command=nivelt_al_esp3)

    # label com o nivel de turma do aluno 3 de espanhol
    lbl_nivelt_al_esp3 = Label(janela_turma_espanhol, text=nivelt, bg="white", font="Arial, 17")

    # posicionamento dos objetos do aluno 3
    add_al_esp3.place(x=20, y=140)
    lbl_nome_al_esp3.place(x=120, y=145)

    add_nota_esp3.place(x=600, y=140)
    lbl_nota_al_esp3.place(x=700, y=145)

    presenc_al_esp3.place(x=770, y=140)
    lbl_presenc_al_esp3.place(x=900, y=145)

    lbl_nome_nv_al_esp3.place(x=950, y=145)
    lbl_nv_al_esp3.place(x=1050, y=145)

    bt_nv_turma_al_esp3.place(x=1100, y=140)
    lbl_nivelt_al_esp3.place(x=1205, y=145)
    #####################################################################
    # fim da estrutura do aluno 3
    #####################################################################

    #####################################################################
    #####################################################################
    #####################################################################

    # estrutura dedicada ao aluno 4 de espanhol
    #####################################################################
    # botão que muda o nome do aluno 4 de espanhol
    add_al_esp4 = Button(janela_turma_espanhol, bg="green", fg="white", width=6, height=1, text="aluno 4:",
                         font="Arial, 15", command=nome_al_esp4)

    # ve o label nome do aluno 4 de espanhol no banco de dados

    arquivo = open('bd_al_esp4.pck', 'rb')
    bd_al_esp4 = pickle.load(arquivo)

    txt_nome_al_esp4 = bd_al_esp4["nome"]
    txt_nota_al_esp4 = bd_al_esp4["nota"]
    txt_presenc_al_esp4 = bd_al_esp4["presenc"]
    nivelt = bd_al_esp4["nivelt"]
    nv_al_esp4 = int(bd_al_esp4["nota"]) // 2
    arquivo.close()

    # label com o nome do aluno 4 de espanhol
    lbl_nome_al_esp4 = Label(janela_turma_espanhol, text=txt_nome_al_esp4, bg="white", font="Arial, 15")

    # botão que muda a nota do aluno 4 de espanhol
    add_nota_esp4 = Button(janela_turma_espanhol, bg="green", fg="white", width=6, height=1, text="Nota: ",
                           font="Arial, 15", command=nota_al_esp4)

    # label com a nota do aluno 4 de espanhol
    lbl_nota_al_esp4 = Label(janela_turma_espanhol, text=txt_nota_al_esp4, bg="white", font="Arial, 15")

    # botão que muda a presença do aluno 4 de espanhol
    presenc_al_esp4 = Button(janela_turma_espanhol, bg="green", fg="white", width=8, height=1, text="Presenças: ",
                             font="Arial, 15", command=presenc_al_esp4)

    # label com a presença do aluno 4 de espanhol
    lbl_presenc_al_esp4 = Label(janela_turma_espanhol, text=txt_presenc_al_esp4, bg="white", font="Arial, 15")

    # label com o nome nivel do aluno 4 de espanhol
    lbl_nome_nv_al_esp4 = Label(janela_turma_espanhol, text="Nivel:", width=6, bg="green", fg="white", font="Arial, 17")

    # label com o  nivel do aluno 4 de espanhol
    lbl_nv_al_esp4 = Label(janela_turma_espanhol, text=nv_al_esp4, bg="white", font="Arial, 17")

    # botão que muda o nome nivel de turma do aluno 4 de espanhol
    bt_nv_turma_al_esp4 = Button(janela_turma_espanhol, bg="green", fg="white", width=6, height=1, text="Nivel T: ",
                                 font="Arial, 15", command=nivelt_al_esp4)

    # label com o nivel de turma do aluno 4 de espanhol
    lbl_nivelt_al_esp4 = Label(janela_turma_espanhol, text=nivelt, bg="white", font="Arial, 17")

    # posicionamento dos objetos do aluno 4
    add_al_esp4.place(x=20, y=200)
    lbl_nome_al_esp4.place(x=120, y=205)

    add_nota_esp4.place(x=600, y=200)
    lbl_nota_al_esp4.place(x=700, y=205)

    presenc_al_esp4.place(x=770, y=200)
    lbl_presenc_al_esp4.place(x=900, y=205)

    lbl_nome_nv_al_esp4.place(x=950, y=205)
    lbl_nv_al_esp4.place(x=1050, y=205)

    bt_nv_turma_al_esp4.place(x=1100, y=200)
    lbl_nivelt_al_esp4.place(x=1205, y=205)

    #####################################################################
    # fim da estrutura do aluno 4
    #####################################################################

    #####################################################################
    #####################################################################
    #####################################################################

    # estrutura dedicada ao aluno 5 de espanhol
    #####################################################################
    # botão que muda o nome do aluno 5 de espanhol
    add_al_esp5 = Button(janela_turma_espanhol, bg="green", fg="white", width=6, height=1, text="aluno 5:",
                         font="Arial, 15", command=nome_al_esp5)

    # ve o label nome do aluno 5 de espanhol no banco de dados

    arquivo = open('bd_al_esp5.pck', 'rb')
    bd_al_esp5 = pickle.load(arquivo)

    txt_nome_al_esp5 = bd_al_esp5["nome"]
    txt_nota_al_esp5 = bd_al_esp5["nota"]
    txt_presenc_al_esp5 = bd_al_esp5["presenc"]
    nivelt = bd_al_esp5["nivelt"]
    nv_al_esp5 = int(bd_al_esp5["nota"]) // 2
    arquivo.close()

    # label com o nome do aluno 5 de espanhol
    lbl_nome_al_esp5 = Label(janela_turma_espanhol, text=txt_nome_al_esp5, bg="white", font="Arial, 15")

    # botão que muda a nota do aluno 5 de espanhol
    add_nota_esp5 = Button(janela_turma_espanhol, bg="green", fg="white", width=6, height=1, text="Nota: ",
                           font="Arial, 15", command=nota_al_esp5)

    # label com a nota do aluno 5 de espanhol
    lbl_nota_al_esp5 = Label(janela_turma_espanhol, text=txt_nota_al_esp5, bg="white", font="Arial, 15")

    # botão que muda a presença do aluno 5 de espanhol
    presenc_al_esp5 = Button(janela_turma_espanhol, bg="green", fg="white", width=8, height=1, text="Presenças: ",
                             font="Arial, 15", command=presenc_al_esp5)

    # label com a presença do aluno 5 de espanhol
    lbl_presenc_al_esp5 = Label(janela_turma_espanhol, text=txt_presenc_al_esp5, bg="white", font="Arial, 15")

    # label com o nome nivel do aluno 5 de espanhol
    lbl_nome_nv_al_esp5 = Label(janela_turma_espanhol, text="Nivel:", width=6, bg="green", fg="white", font="Arial, 17")

    # label com o  nivel do aluno 5 de espanhol
    lbl_nv_al_esp5 = Label(janela_turma_espanhol, text=nv_al_esp5, bg="white", font="Arial, 17")

    # botão que muda o nome nivel de turma do aluno 5 de espanhol
    bt_nv_turma_al_esp5 = Button(janela_turma_espanhol, bg="green", fg="white", width=6, height=1, text="Nivel T: ",
                                 font="Arial, 15", command=nivelt_al_esp5)

    # label com o nivel de turma do aluno 5 de espanhol
    lbl_nivelt_al_esp5 = Label(janela_turma_espanhol, text=nivelt, bg="white", font="Arial, 17")

    # posicionamento dos objetos do aluno 5
    add_al_esp5.place(x=20, y=250)
    lbl_nome_al_esp5.place(x=120, y=255)

    add_nota_esp5.place(x=600, y=250)
    lbl_nota_al_esp5.place(x=700, y=255)

    presenc_al_esp5.place(x=770, y=250)
    lbl_presenc_al_esp5.place(x=900, y=255)

    lbl_nome_nv_al_esp5.place(x=950, y=255)
    lbl_nv_al_esp5.place(x=1050, y=255)

    bt_nv_turma_al_esp5.place(x=1100, y=250)
    lbl_nivelt_al_esp5.place(x=1205, y=255)

    #####################################################################
    # fim da estrutura do aluno 5
    #####################################################################

    #####################################################################
    #####################################################################
    #####################################################################

    # estrutura dedicada ao aluno 6 de espanhol
    #####################################################################
    # botão que muda o nome do aluno 6 de espanhol
    add_al_esp6 = Button(janela_turma_espanhol, bg="green", fg="white", width=6, height=1, text="aluno 6:",
                         font="Arial, 15", command=nome_al_esp6)

    # ve o label nome do aluno 6 de espanhol no banco de dados

    arquivo = open('bd_al_esp6.pck', 'rb')
    bd_al_esp6 = pickle.load(arquivo)

    txt_nome_al_esp6 = bd_al_esp6["nome"]
    txt_nota_al_esp6 = bd_al_esp6["nota"]
    txt_presenc_al_esp6 = bd_al_esp6["presenc"]
    nivelt = bd_al_esp6["nivelt"]
    nv_al_esp6 = int(bd_al_esp6["nota"]) // 2
    arquivo.close()

    # label com o nome do aluno 6 de espanhol
    lbl_nome_al_esp6 = Label(janela_turma_espanhol, text=txt_nome_al_esp6, bg="white", font="Arial, 15")

    # botão que muda a nota do aluno 6 de espanhol
    add_nota_esp6 = Button(janela_turma_espanhol, bg="green", fg="white", width=6, height=1, text="Nota: ",
                           font="Arial, 15", command=nota_al_esp6)

    # label com a nota do aluno 6 de espanhol
    lbl_nota_al_esp6 = Label(janela_turma_espanhol, text=txt_nota_al_esp6, bg="white", font="Arial, 15")

    # botão que muda a presença do aluno 6 de espanhol
    presenc_al_esp6 = Button(janela_turma_espanhol, bg="green", fg="white", width=8, height=1, text="Presenças: ",
                             font="Arial, 15", command=presenc_al_esp6)

    # label com a presença do aluno 6 de espanhol
    lbl_presenc_al_esp6 = Label(janela_turma_espanhol, text=txt_presenc_al_esp6, bg="white", font="Arial, 15")

    # label com o nome nivel do aluno 6 de espanhol
    lbl_nome_nv_al_esp6 = Label(janela_turma_espanhol, text="Nivel:", width=6, bg="green", fg="white", font="Arial, 17")

    # label com o  nivel do aluno 6 de espanhol
    lbl_nv_al_esp6 = Label(janela_turma_espanhol, text=nv_al_esp6, bg="white", font="Arial, 17")

    # botão que muda o nome nivel de turma do aluno 6 de espanhol
    bt_nv_turma_al_esp6 = Button(janela_turma_espanhol, bg="green", fg="white", width=6, height=1, text="Nivel T: ",
                                 font="Arial, 15", command=nivelt_al_esp6)

    # label com o nivel de turma do aluno 6 de espanhol
    lbl_nivelt_al_esp6 = Label(janela_turma_espanhol, text=nivelt, bg="white", font="Arial, 17")

    # posicionamento dos objetos do aluno 6
    add_al_esp6.place(x=20, y=300)
    lbl_nome_al_esp6.place(x=120, y=305)

    add_nota_esp6.place(x=600, y=300)
    lbl_nota_al_esp6.place(x=700, y=305)

    presenc_al_esp6.place(x=770, y=300)
    lbl_presenc_al_esp6.place(x=900, y=305)

    lbl_nome_nv_al_esp6.place(x=950, y=305)
    lbl_nv_al_esp6.place(x=1050, y=305)

    bt_nv_turma_al_esp6.place(x=1100, y=300)
    lbl_nivelt_al_esp6.place(x=1205, y=305)

    #####################################################################
    # fim da estrutura do aluno 6
    #####################################################################

    #####################################################################
    #####################################################################
    #####################################################################

    # estrutura dedicada ao aluno 7 de espanhol
    #####################################################################
    # botão que muda o nome do aluno 7 de espanhol
    add_al_esp7 = Button(janela_turma_espanhol, bg="green", fg="white", width=6, height=1, text="aluno 7:",
                         font="Arial, 15", command=nome_al_esp7)

    # ve o label nome do aluno 7 de espanhol no banco de dados

    arquivo = open('bd_al_esp7.pck', 'rb')
    bd_al_esp7 = pickle.load(arquivo)

    txt_nome_al_esp7 = bd_al_esp7["nome"]
    txt_nota_al_esp7 = bd_al_esp7["nota"]
    txt_presenc_al_esp7 = bd_al_esp7["presenc"]
    nivelt = bd_al_esp7["nivelt"]
    nv_al_esp7 = int(bd_al_esp7["nota"]) // 2
    arquivo.close()

    # label com o nome do aluno 7 de espanhol
    lbl_nome_al_esp7 = Label(janela_turma_espanhol, text=txt_nome_al_esp7, bg="white", font="Arial, 15")

    # botão que muda a nota do aluno 7 de espanhol
    add_nota_esp7 = Button(janela_turma_espanhol, bg="green", fg="white", width=6, height=1, text="Nota: ",
                           font="Arial, 15", command=nota_al_esp7)

    # label com a nota do aluno 7 de espanhol
    lbl_nota_al_esp7 = Label(janela_turma_espanhol, text=txt_nota_al_esp7, bg="white", font="Arial, 15")

    # botão que muda a presença do aluno 7 de espanhol
    presenc_al_esp7 = Button(janela_turma_espanhol, bg="green", fg="white", width=8, height=1, text="Presenças: ",
                             font="Arial, 15", command=presenc_al_esp7)

    # label com a presença do aluno 7 de espanhol
    lbl_presenc_al_esp7 = Label(janela_turma_espanhol, text=txt_presenc_al_esp7, bg="white", font="Arial, 15")

    # label com o nome nivel do aluno 7 de espanhol
    lbl_nome_nv_al_esp7 = Label(janela_turma_espanhol, text="Nivel:", width=6, bg="green", fg="white", font="Arial, 17")

    # label com o  nivel do aluno 7 de espanhol
    lbl_nv_al_esp7 = Label(janela_turma_espanhol, text=nv_al_esp7, bg="white", font="Arial, 17")

    # botão que muda o nome nivel de turma do aluno 7 de espanhol
    bt_nv_turma_al_esp7 = Button(janela_turma_espanhol, bg="green", fg="white", width=6, height=1, text="Nivel T: ",
                                 font="Arial, 15", command=nivelt_al_esp7)

    # label com o nivel de turma do aluno 7 de espanhol
    lbl_nivelt_al_esp7 = Label(janela_turma_espanhol, text=nivelt, bg="white", font="Arial, 17")

    # posicionamento dos objetos do aluno 7
    add_al_esp7.place(x=20, y=350)
    lbl_nome_al_esp7.place(x=120, y=355)

    add_nota_esp7.place(x=600, y=350)
    lbl_nota_al_esp7.place(x=700, y=355)

    presenc_al_esp7.place(x=770, y=350)
    lbl_presenc_al_esp7.place(x=900, y=355)

    lbl_nome_nv_al_esp7.place(x=950, y=355)
    lbl_nv_al_esp7.place(x=1050, y=355)

    bt_nv_turma_al_esp7.place(x=1100, y=350)
    lbl_nivelt_al_esp7.place(x=1205, y=355)

    #####################################################################
    # fim da estrutura do aluno 7
    #####################################################################

    #####################################################################
    #####################################################################
    #####################################################################

    # estrutura dedicada ao aluno 8 de espanhol
    #####################################################################
    # botão que muda o nome do aluno 8 de espanhol
    add_al_esp8 = Button(janela_turma_espanhol, bg="green", fg="white", width=6, height=1, text="aluno 8:",
                         font="Arial, 15", command=nome_al_esp8)

    # ve o label nome do aluno 8 de espanhol no banco de dados

    arquivo = open('bd_al_esp8.pck', 'rb')
    bd_al_esp8 = pickle.load(arquivo)

    txt_nome_al_esp8 = bd_al_esp8["nome"]
    txt_nota_al_esp8 = bd_al_esp8["nota"]
    txt_presenc_al_esp8 = bd_al_esp8["presenc"]
    nivelt = bd_al_esp8["nivelt"]
    nv_al_esp8 = int(bd_al_esp8["nota"]) // 2
    arquivo.close()

    # label com o nome do aluno 8 de espanhol
    lbl_nome_al_esp8 = Label(janela_turma_espanhol, text=txt_nome_al_esp8, bg="white", font="Arial, 15")

    # botão que muda a nota do aluno 8 de espanhol
    add_nota_esp8 = Button(janela_turma_espanhol, bg="green", fg="white", width=6, height=1, text="Nota: ",
                           font="Arial, 15", command=nota_al_esp8)

    # label com a nota do aluno 8 de espanhol
    lbl_nota_al_esp8 = Label(janela_turma_espanhol, text=txt_nota_al_esp8, bg="white", font="Arial, 15")

    # botão que muda a presença do aluno 8 de espanhol
    presenc_al_esp8 = Button(janela_turma_espanhol, bg="green", fg="white", width=8, height=1, text="Presenças: ",
                             font="Arial, 15", command=presenc_al_esp8)

    # label com a presença do aluno 8 de espanhol
    lbl_presenc_al_esp8 = Label(janela_turma_espanhol, text=txt_presenc_al_esp8, bg="white", font="Arial, 15")

    # label com o nome nivel do aluno 8 de espanhol
    lbl_nome_nv_al_esp8 = Label(janela_turma_espanhol, text="Nivel:", width=6, bg="green", fg="white", font="Arial, 17")

    # label com o  nivel do aluno 8 de espanhol
    lbl_nv_al_esp8 = Label(janela_turma_espanhol, text=nv_al_esp8, bg="white", font="Arial, 17")

    # botão que muda o nome nivel de turma do aluno 8 de espanhol
    bt_nv_turma_al_esp8 = Button(janela_turma_espanhol, bg="green", fg="white", width=6, height=1, text="Nivel T: ",
                                 font="Arial, 15", command=nivelt_al_esp8)

    # label com o nivel de turma do aluno 8 de espanhol
    lbl_nivelt_al_esp8 = Label(janela_turma_espanhol, text=nivelt, bg="white", font="Arial, 17")

    # posicionamento dos objetos do aluno 8
    add_al_esp8.place(x=20, y=400)
    lbl_nome_al_esp8.place(x=120, y=405)

    add_nota_esp8.place(x=600, y=400)
    lbl_nota_al_esp8.place(x=700, y=405)

    presenc_al_esp8.place(x=770, y=400)
    lbl_presenc_al_esp8.place(x=900, y=405)

    lbl_nome_nv_al_esp8.place(x=950, y=405)
    lbl_nv_al_esp8.place(x=1050, y=405)

    bt_nv_turma_al_esp8.place(x=1100, y=400)
    lbl_nivelt_al_esp8.place(x=1205, y=405)

    #####################################################################
    # fim da estrutura do aluno 8
    #####################################################################

    #####################################################################
    #####################################################################
    #####################################################################

    # estrutura dedicada ao aluno 9 de espanhol
    #####################################################################
    # botão que muda o nome do aluno 9 de espanhol
    add_al_esp9 = Button(janela_turma_espanhol, bg="green", fg="white", width=6, height=1, text="aluno 9:",
                         font="Arial, 15", command=nome_al_esp9)

    # ve o label nome do aluno 9 de espanhol no banco de dados

    arquivo = open('bd_al_esp9.pck', 'rb')
    bd_al_esp9 = pickle.load(arquivo)

    txt_nome_al_esp9 = bd_al_esp9["nome"]
    txt_nota_al_esp9 = bd_al_esp9["nota"]
    txt_presenc_al_esp9 = bd_al_esp9["presenc"]
    nivelt = bd_al_esp9["nivelt"]
    nv_al_esp9 = int(bd_al_esp9["nota"]) // 2
    arquivo.close()

    # label com o nome do aluno 9 de espanhol
    lbl_nome_al_esp9 = Label(janela_turma_espanhol, text=txt_nome_al_esp9, bg="white", font="Arial, 15")

    # botão que muda a nota do aluno 9 de espanhol
    add_nota_esp9 = Button(janela_turma_espanhol, bg="green", fg="white", width=6, height=1, text="Nota: ",
                           font="Arial, 15", command=nota_al_esp9)

    # label com a nota do aluno 9 de espanhol
    lbl_nota_al_esp9 = Label(janela_turma_espanhol, text=txt_nota_al_esp9, bg="white", font="Arial, 15")

    # botão que muda a presença do aluno 9 de espanhol
    presenc_al_esp9 = Button(janela_turma_espanhol, bg="green", fg="white", width=8, height=1, text="Presenças: ",
                             font="Arial, 15", command=presenc_al_esp9)

    # label com a presença do aluno 9 de espanhol
    lbl_presenc_al_esp9 = Label(janela_turma_espanhol, text=txt_presenc_al_esp9, bg="white", font="Arial, 15")

    # label com o nome nivel do aluno 9 de espanhol
    lbl_nome_nv_al_esp9 = Label(janela_turma_espanhol, text="Nivel:", width=6, bg="green", fg="white", font="Arial, 17")

    # label com o  nivel do aluno 9 de espanhol
    lbl_nv_al_esp9 = Label(janela_turma_espanhol, text=nv_al_esp9, bg="white", font="Arial, 17")

    # botão que muda o nome nivel de turma do aluno 9 de espanhol
    bt_nv_turma_al_esp9 = Button(janela_turma_espanhol, bg="green", fg="white", width=6, height=1, text="Nivel T: ",
                                 font="Arial, 15", command=nivelt_al_esp9)

    # label com o nivel de turma do aluno 9 de espanhol
    lbl_nivelt_al_esp9 = Label(janela_turma_espanhol, text=nivelt, bg="white", font="Arial, 17")

    # posicionamento dos objetos do aluno 9
    add_al_esp9.place(x=20, y=450)
    lbl_nome_al_esp9.place(x=120, y=455)

    add_nota_esp9.place(x=600, y=450)
    lbl_nota_al_esp9.place(x=700, y=455)

    presenc_al_esp9.place(x=770, y=450)
    lbl_presenc_al_esp9.place(x=900, y=455)

    lbl_nome_nv_al_esp9.place(x=950, y=455)
    lbl_nv_al_esp9.place(x=1050, y=455)

    bt_nv_turma_al_esp9.place(x=1100, y=450)
    lbl_nivelt_al_esp9.place(x=1205, y=455)

    #####################################################################
    # fim da estrutura do aluno 9
    #####################################################################

    #####################################################################
    #####################################################################
    #####################################################################

    # estrutura dedicada ao aluno 10 de espanhol
    #####################################################################
    # botão que muda o nome do aluno 10 de espanhol
    add_al_esp10 = Button(janela_turma_espanhol, bg="green", fg="white", width=6, height=1, text="aluno 10:",
                          font="Arial, 15", command=nome_al_esp10)

    # ve o label nome do aluno 10 de espanhol no banco de dados

    arquivo = open('bd_al_esp10.pck', 'rb')
    bd_al_esp10 = pickle.load(arquivo)

    txt_nome_al_esp10 = bd_al_esp10["nome"]
    txt_nota_al_esp10 = bd_al_esp10["nota"]
    txt_presenc_al_esp10 = bd_al_esp10["presenc"]
    nivelt = bd_al_esp10["nivelt"]
    nv_al_esp10 = int(bd_al_esp10["nota"]) // 2
    arquivo.close()

    # label com o nome do aluno 10 de espanhol
    lbl_nome_al_esp10 = Label(janela_turma_espanhol, text=txt_nome_al_esp10, bg="white", font="Arial, 15")

    # botão que muda a nota do aluno 10 de espanhol
    add_nota_esp10 = Button(janela_turma_espanhol, bg="green", fg="white", width=6, height=1, text="Nota: ",
                            font="Arial, 15", command=nota_al_esp10)

    # label com a nota do aluno 10 de espanhol
    lbl_nota_al_esp10 = Label(janela_turma_espanhol, text=txt_nota_al_esp10, bg="white", font="Arial, 15")

    # botão que muda a presença do aluno 10 de espanhol
    presenc_al_esp10 = Button(janela_turma_espanhol, bg="green", fg="white", width=8, height=1, text="Presenças: ",
                              font="Arial, 15", command=presenc_al_esp10)

    # label com a presença do aluno 10 de espanhol
    lbl_presenc_al_esp10 = Label(janela_turma_espanhol, text=txt_presenc_al_esp10, bg="white", font="Arial, 15")

    # label com o nome nivel do aluno 10 de espanhol
    lbl_nome_nv_al_esp10 = Label(janela_turma_espanhol, text="Nivel:", width=6, bg="green", fg="white",
                                 font="Arial, 17")

    # label com o  nivel do aluno 10 de espanhol
    lbl_nv_al_esp10 = Label(janela_turma_espanhol, text=nv_al_esp10, bg="white", font="Arial, 17")

    # botão que muda o nome nivel de turma do aluno 10 de espanhol
    bt_nv_turma_al_esp10 = Button(janela_turma_espanhol, bg="green", fg="white", width=6, height=1, text="Nivel T: ",
                                  font="Arial, 15", command=nivelt_al_esp10)

    # label com o nivel de turma do aluno 10 de espanhol
    lbl_nivelt_al_esp10 = Label(janela_turma_espanhol, text=nivelt, bg="white", font="Arial, 17")

    # posicionamento dos objetos do aluno 10
    add_al_esp10.place(x=20, y=500)
    lbl_nome_al_esp10.place(x=120, y=505)

    add_nota_esp10.place(x=600, y=500)
    lbl_nota_al_esp10.place(x=700, y=505)

    presenc_al_esp10.place(x=770, y=500)
    lbl_presenc_al_esp10.place(x=900, y=505)

    lbl_nome_nv_al_esp10.place(x=950, y=505)
    lbl_nv_al_esp10.place(x=1050, y=505)

    bt_nv_turma_al_esp10.place(x=1100, y=500)
    lbl_nivelt_al_esp10.place(x=1205, y=505)

    #####################################################################
    # fim da estrutura do aluno 10
    #####################################################################

    #####################################################################
    #####################################################################
    #####################################################################
    #####################################################################
    # barra de rolagem lateral direita
    sb = Scrollbar(janela_turma_espanhol)
    sb.pack(side='right', fill=Y)
    janela_turma_espanhol.mainloop()


#####################################################################
# parte do programa dedicada ao aluno 1 de espanhol
#####################################################################

def nome_al_esp1():
    global nome_esp1, tela
    tela = Tk()
    tela.configure(bg="white")
    tela.geometry("775x100+50+100")
    tela.title("Entrada do nome do aluno")

    nome_esp1 = Entry(tela, width=50, font="Arial, 20")
    nome_esp1.place(x=10, y=25)

    bt_salva = Button(tela, text="Salvar", bg="blue", fg="white", font="Arial, 15", command=salvar_nome_esp1)
    bt_salva.place(x=600, y=60)

    tela.mainloop()


def salvar_nome_esp1():
    global nome_esp1, lbl_nome_al_esp1, tela
    nome = nome_esp1.get().title()
    tela.destroy()

    arquivo = open('bd_al_esp1.pck', 'rb')
    bd_al_esp1 = pickle.load(arquivo)
    arquivo.close()

    bd_al_esp1["nome"] = nome
    arquivo = open('bd_al_esp1.pck', 'wb')
    pickle.dump(bd_al_esp1, arquivo)
    arquivo.close()
    lbl_nome_al_esp1["text"] = nome


def nota_al_esp1():
    global nota_esp1, tela, lbl_msg_nota_al_esp1
    tela = Tk()
    tela.configure(bg="white")
    tela.geometry("775x100+50+100")
    tela.title("Entrada do nome do aluno")

    nota_esp1 = Entry(tela, width=50, font="Arial, 20")

    bt_salva = Button(tela, text="Salvar", bg="blue", fg="white", font="Arial, 15", command=salvar_nota_esp1)

    lbl_msg_nota_al_esp1 = Label(tela, text="Digite a nota do aluno(valor entre 0 e 10)", bg="green", fg="white",
                                 font="Arial, 15")

    nota_esp1.place(x=10, y=25)
    bt_salva.place(x=600, y=60)
    lbl_msg_nota_al_esp1.place(x=15, y=65)
    tela.mainloop()


def salvar_nota_esp1():
    global nota_esp1, lbl_nota_al_esp1, tela, lbl_nv_al_esp1, lbl_msg_nota_al_esp1
    note = int(nota_esp1.get())
    nota = nota_esp1.get()
    lbl = note // 2

    if note < 0 or note > 10:
        lbl_msg_nota_al_esp1["text"] = "ERRO! a nota do aluno deve ser um numero entre 0 e 10"
        lbl_msg_nota_al_esp1["bg"] = "red"
        raise Exception
    elif note >= 0 and note <= 10:
        tela.destroy()
        arquivo = open('bd_al_esp1.pck', 'rb')
        bd_al_esp1 = pickle.load(arquivo)
        arquivo.close()

        bd_al_esp1["nota"] = nota

        arquivo = open('bd_al_esp1.pck', 'wb')
        pickle.dump(bd_al_esp1, arquivo)
        arquivo.close()

        lbl_nota_al_esp1["text"] = str(nota)
        lbl_nv_al_esp1["text"] = str(lbl)


def presenc_al_esp1():
    global presenc_esp1, tela
    tela = Tk()
    tela.configure(bg="white")
    tela.geometry("775x100+50+100")
    tela.title("Entrada das presenças do aluno")

    presenc_esp1 = Entry(tela, width=50, font="Arial, 20")
    presenc_esp1.place(x=10, y=25)

    bt_salva = Button(tela, text="Salvar", bg="blue", fg="white", font="Arial, 15", command=salvar_presenc_esp1)
    bt_salva.place(x=600, y=60)

    tela.mainloop()


def salvar_presenc_esp1():
    global presenc_esp1, lbl_presenc_al_esp1, tela
    presenc = presenc_esp1.get()
    note = int(presenc_esp1.get())
    tela.destroy()

    arquivo = open('bd_al_esp1.pck', 'rb')
    bd_al_esp1 = pickle.load(arquivo)
    arquivo.close()

    bd_al_esp1["presenc"] = presenc

    arquivo = open('bd_al_esp1.pck', 'wb')
    lbl_presenc_al_esp1["text"] = presenc
    pickle.dump(bd_al_esp1, arquivo)
    arquivo.close()


def nivelt_al_esp1():
    global nivelt_esp1, tela
    tela = Tk()
    tela.configure(bg="white")
    tela.geometry("775x100+50+100")
    tela.title("Entrada do Nivel de Turma do Aluno do aluno")

    nivelt_esp1 = Entry(tela, width=50, font="Arial, 20")
    nivelt_esp1.place(x=10, y=25)

    bt_salva = Button(tela, text="Salvar", bg="blue", fg="white", font="Arial, 15", command=salvar_nivelt_esp1)
    bt_salva.place(x=600, y=60)

    tela.mainloop()


def salvar_nivelt_esp1():
    global nivelt_esp1, lbl_nivelt_al_esp1, tela
    nivelt = nivelt_esp1.get()
    tela.destroy()

    arquivo = open('bd_al_esp1.pck', 'rb')
    bd_al_esp1 = pickle.load(arquivo)
    arquivo.close()

    bd_al_esp1["nivelt"] = nivelt
    arquivo = open('bd_al_esp1.pck', 'wb')
    pickle.dump(bd_al_esp1, arquivo)
    arquivo.close()

    lbl_nivelt_al_esp1["text"] = nivelt


#####################################################################
# fim parte do programa dedicada ao aluno 1 de espanhol
#####################################################################

#####################################################################
#####################################################################
#####################################################################



#####################################################################
# parte do programa dedicada ao aluno 2 de espanhol
#####################################################################

def nome_al_esp2():
    global nome_esp2, tela
    tela = Tk()
    tela.configure(bg="white")
    tela.geometry("775x100+50+100")
    tela.title("Entrada do nome do aluno")

    nome_esp2 = Entry(tela, width=50, font="Arial, 20")
    nome_esp2.place(x=10, y=25)

    bt_salva = Button(tela, text="Salvar", bg="blue", fg="white", font="Arial, 15", command=salvar_nome_esp2)
    bt_salva.place(x=600, y=60)

    tela.mainloop()


def salvar_nome_esp2():
    global nome_esp2, lbl_nome_al_esp2, tela
    nome = nome_esp2.get().title()
    tela.destroy()

    arquivo = open('bd_al_esp2.pck', 'rb')
    bd_al_esp2 = pickle.load(arquivo)
    arquivo.close()

    bd_al_esp2["nome"] = nome
    arquivo = open('bd_al_esp2.pck', 'wb')
    pickle.dump(bd_al_esp2, arquivo)
    arquivo.close()
    lbl_nome_al_esp2["text"] = nome


def nota_al_esp2():
    global nota_esp2, tela, lbl_msg_nota_al_esp2
    tela = Tk()
    tela.configure(bg="white")
    tela.geometry("775x100+50+100")
    tela.title("Entrada do nome do aluno")

    nota_esp2 = Entry(tela, width=50, font="Arial, 20")

    bt_salva = Button(tela, text="Salvar", bg="blue", fg="white", font="Arial, 15", command=salvar_nota_esp2)

    lbl_msg_nota_al_esp2 = Label(tela, text="Digite a nota do aluno(valor entre 0 e 10)", bg="green", fg="white",
                                 font="Arial, 15")

    nota_esp2.place(x=10, y=25)
    bt_salva.place(x=600, y=60)
    lbl_msg_nota_al_esp2.place(x=15, y=65)
    tela.mainloop()


def salvar_nota_esp2():
    global nota_esp2, lbl_nota_al_esp2, tela, lbl_nv_al_esp2, lbl_msg_nota_al_esp2
    note = int(nota_esp2.get())
    nota = nota_esp2.get()
    lbl = note // 2

    if note < 0 or note > 10:
        lbl_msg_nota_al_esp2["text"] = "ERRO! a nota do aluno deve ser um numero entre 0 e 10"
        lbl_msg_nota_al_esp2["bg"] = "red"
        raise Exception
    elif note >= 0 and note <= 10:
        tela.destroy()
        arquivo = open('bd_al_esp2.pck', 'rb')
        bd_al_esp2 = pickle.load(arquivo)
        arquivo.close()

        bd_al_esp2["nota"] = nota

        arquivo = open('bd_al_esp2.pck', 'wb')
        pickle.dump(bd_al_esp2, arquivo)
        arquivo.close()

        lbl_nota_al_esp2["text"] = str(nota)
        lbl_nv_al_esp2["text"] = str(lbl)


def presenc_al_esp2():
    global presenc_esp2, tela
    tela = Tk()
    tela.configure(bg="white")
    tela.geometry("775x100+50+100")
    tela.title("Entrada das presenças do aluno")

    presenc_esp2 = Entry(tela, width=50, font="Arial, 20")
    presenc_esp2.place(x=10, y=25)

    bt_salva = Button(tela, text="Salvar", bg="blue", fg="white", font="Arial, 15", command=salvar_presenc_esp2)
    bt_salva.place(x=600, y=60)

    tela.mainloop()


def salvar_presenc_esp2():
    global presenc_esp2, lbl_presenc_al_esp2, tela
    presenc = presenc_esp2.get()
    note = int(presenc_esp2.get())
    tela.destroy()

    arquivo = open('bd_al_esp2.pck', 'rb')
    bd_al_esp2 = pickle.load(arquivo)
    arquivo.close()

    bd_al_esp2["presenc"] = presenc

    arquivo = open('bd_al_esp2.pck', 'wb')
    lbl_presenc_al_esp2["text"] = presenc
    pickle.dump(bd_al_esp2, arquivo)
    arquivo.close()


def nivelt_al_esp2():
    global nivelt_esp2, tela
    tela = Tk()
    tela.configure(bg="white")
    tela.geometry("775x100+50+100")
    tela.title("Entrada do Nivel de Turma do Aluno do aluno")

    nivelt_esp2 = Entry(tela, width=50, font="Arial, 20")
    nivelt_esp2.place(x=10, y=25)

    bt_salva = Button(tela, text="Salvar", bg="blue", fg="white", font="Arial, 15", command=salvar_nivelt_esp2)
    bt_salva.place(x=600, y=60)

    tela.mainloop()


def salvar_nivelt_esp2():
    global nivelt_esp2, lbl_nivelt_al_esp2, tela
    nivelt = nivelt_esp2.get()
    tela.destroy()

    arquivo = open('bd_al_esp2.pck', 'rb')
    bd_al_esp2 = pickle.load(arquivo)
    arquivo.close()

    bd_al_esp2["nivelt"] = nivelt
    arquivo = open('bd_al_esp2.pck', 'wb')
    pickle.dump(bd_al_esp2, arquivo)
    arquivo.close()

    lbl_nivelt_al_esp2["text"] = nivelt


#####################################################################
# fim parte do programa dedicada ao aluno 2 de espanhol
#####################################################################

#####################################################################
#####################################################################
#####################################################################



#####################################################################
# parte do programa dedicada ao aluno 3 de espanhol
#####################################################################

def nome_al_esp3():
    global nome_esp3, tela
    tela = Tk()
    tela.configure(bg="white")
    tela.geometry("775x100+50+100")
    tela.title("Entrada do nome do aluno")

    nome_esp3 = Entry(tela, width=50, font="Arial, 20")
    nome_esp3.place(x=10, y=25)

    bt_salva = Button(tela, text="Salvar", bg="blue", fg="white", font="Arial, 15", command=salvar_nome_esp3)
    bt_salva.place(x=600, y=60)

    tela.mainloop()


def salvar_nome_esp3():
    global nome_esp3, lbl_nome_al_esp3, tela
    nome = nome_esp3.get().title()
    tela.destroy()

    arquivo = open('bd_al_esp3.pck', 'rb')
    bd_al_esp3 = pickle.load(arquivo)
    arquivo.close()

    bd_al_esp3["nome"] = nome
    arquivo = open('bd_al_esp3.pck', 'wb')
    pickle.dump(bd_al_esp3, arquivo)
    arquivo.close()
    lbl_nome_al_esp3["text"] = nome


def nota_al_esp3():
    global nota_esp3, tela, lbl_msg_nota_al_esp3
    tela = Tk()
    tela.configure(bg="white")
    tela.geometry("775x100+50+100")
    tela.title("Entrada do nome do aluno")

    nota_esp3 = Entry(tela, width=50, font="Arial, 20")

    bt_salva = Button(tela, text="Salvar", bg="blue", fg="white", font="Arial, 15", command=salvar_nota_esp3)

    lbl_msg_nota_al_esp3 = Label(tela, text="Digite a nota do aluno(valor entre 0 e 10)", bg="green", fg="white",
                                 font="Arial, 15")

    nota_esp3.place(x=10, y=25)
    bt_salva.place(x=600, y=60)
    lbl_msg_nota_al_esp3.place(x=15, y=65)
    tela.mainloop()


def salvar_nota_esp3():
    global nota_esp3, lbl_nota_al_esp3, tela, lbl_nv_al_esp3, lbl_msg_nota_al_esp3
    note = int(nota_esp3.get())
    nota = nota_esp3.get()
    lbl = note // 2

    if note < 0 or note > 10:
        lbl_msg_nota_al_esp3["text"] = "ERRO! a nota do aluno deve ser um numero entre 0 e 10"
        lbl_msg_nota_al_esp3["bg"] = "red"
        raise Exception
    elif note >= 0 and note <= 10:
        tela.destroy()
        arquivo = open('bd_al_esp3.pck', 'rb')
        bd_al_esp3 = pickle.load(arquivo)
        arquivo.close()

        bd_al_esp3["nota"] = nota

        arquivo = open('bd_al_esp3.pck', 'wb')
        pickle.dump(bd_al_esp3, arquivo)
        arquivo.close()

        lbl_nota_al_esp3["text"] = str(nota)
        lbl_nv_al_esp3["text"] = str(lbl)


def presenc_al_esp3():
    global presenc_esp3, tela
    tela = Tk()
    tela.configure(bg="white")
    tela.geometry("775x100+50+100")
    tela.title("Entrada das presenças do aluno")

    presenc_esp3 = Entry(tela, width=50, font="Arial, 20")
    presenc_esp3.place(x=10, y=25)

    bt_salva = Button(tela, text="Salvar", bg="blue", fg="white", font="Arial, 15", command=salvar_presenc_esp3)
    bt_salva.place(x=600, y=60)

    tela.mainloop()


def salvar_presenc_esp3():
    global presenc_esp3, lbl_presenc_al_esp3, tela
    presenc = presenc_esp3.get()
    note = int(presenc_esp3.get())
    tela.destroy()

    arquivo = open('bd_al_esp3.pck', 'rb')
    bd_al_esp3 = pickle.load(arquivo)
    arquivo.close()

    bd_al_esp3["presenc"] = presenc

    arquivo = open('bd_al_esp3.pck', 'wb')
    lbl_presenc_al_esp3["text"] = presenc
    pickle.dump(bd_al_esp3, arquivo)
    arquivo.close()


def nivelt_al_esp3():
    global nivelt_esp3, tela
    tela = Tk()
    tela.configure(bg="white")
    tela.geometry("775x100+50+100")
    tela.title("Entrada do Nivel de Turma do Aluno do aluno")

    nivelt_esp3 = Entry(tela, width=50, font="Arial, 20")
    nivelt_esp3.place(x=10, y=25)

    bt_salva = Button(tela, text="Salvar", bg="blue", fg="white", font="Arial, 15", command=salvar_nivelt_esp3)
    bt_salva.place(x=600, y=60)

    tela.mainloop()


def salvar_nivelt_esp3():
    global nivelt_esp3, lbl_nivelt_al_esp3, tela
    nivelt = nivelt_esp3.get()
    tela.destroy()

    arquivo = open('bd_al_esp3.pck', 'rb')
    bd_al_esp3 = pickle.load(arquivo)
    arquivo.close()

    bd_al_esp3["nivelt"] = nivelt
    arquivo = open('bd_al_esp3.pck', 'wb')
    pickle.dump(bd_al_esp3, arquivo)
    arquivo.close()

    lbl_nivelt_al_esp3["text"] = nivelt


#####################################################################
# fim parte do programa dedicada ao aluno 3 de espanhol
#####################################################################

#####################################################################
#####################################################################
#####################################################################



#####################################################################
# parte do programa dedicada ao aluno 4 de espanhol
#####################################################################

def nome_al_esp4():
    global nome_esp4, tela
    tela = Tk()
    tela.configure(bg="white")
    tela.geometry("775x100+50+100")
    tela.title("Entrada do nome do aluno")

    nome_esp4 = Entry(tela, width=50, font="Arial, 20")
    nome_esp4.place(x=10, y=25)

    bt_salva = Button(tela, text="Salvar", bg="blue", fg="white", font="Arial, 15", command=salvar_nome_esp4)
    bt_salva.place(x=600, y=60)

    tela.mainloop()


def salvar_nome_esp4():
    global nome_esp4, lbl_nome_al_esp4, tela
    nome = nome_esp4.get().title()
    tela.destroy()

    arquivo = open('bd_al_esp4.pck', 'rb')
    bd_al_esp4 = pickle.load(arquivo)
    arquivo.close()

    bd_al_esp4["nome"] = nome
    arquivo = open('bd_al_esp4.pck', 'wb')
    pickle.dump(bd_al_esp4, arquivo)
    arquivo.close()
    lbl_nome_al_esp4["text"] = nome


def nota_al_esp4():
    global nota_esp4, tela, lbl_msg_nota_al_esp4
    tela = Tk()
    tela.configure(bg="white")
    tela.geometry("775x100+50+100")
    tela.title("Entrada do nome do aluno")

    nota_esp4 = Entry(tela, width=50, font="Arial, 20")

    bt_salva = Button(tela, text="Salvar", bg="blue", fg="white", font="Arial, 15", command=salvar_nota_esp4)

    lbl_msg_nota_al_esp4 = Label(tela, text="Digite a nota do aluno(valor entre 0 e 10)", bg="green", fg="white",
                                 font="Arial, 15")

    nota_esp4.place(x=10, y=25)
    bt_salva.place(x=600, y=60)
    lbl_msg_nota_al_esp4.place(x=15, y=65)
    tela.mainloop()


def salvar_nota_esp4():
    global nota_esp4, lbl_nota_al_esp4, tela, lbl_nv_al_esp4, lbl_msg_nota_al_esp4
    note = int(nota_esp4.get())
    nota = nota_esp4.get()
    lbl = note // 2

    if note < 0 or note > 10:
        lbl_msg_nota_al_esp4["text"] = "ERRO! a nota do aluno deve ser um numero entre 0 e 10"
        lbl_msg_nota_al_esp4["bg"] = "red"
        raise Exception
    elif note >= 0 and note <= 10:
        tela.destroy()
        arquivo = open('bd_al_esp4.pck', 'rb')
        bd_al_esp4 = pickle.load(arquivo)
        arquivo.close()

        bd_al_esp4["nota"] = nota

        arquivo = open('bd_al_esp4.pck', 'wb')
        pickle.dump(bd_al_esp4, arquivo)
        arquivo.close()

        lbl_nota_al_esp4["text"] = str(nota)
        lbl_nv_al_esp4["text"] = str(lbl)


def presenc_al_esp4():
    global presenc_esp4, tela
    tela = Tk()
    tela.configure(bg="white")
    tela.geometry("775x100+50+100")
    tela.title("Entrada das presenças do aluno")

    presenc_esp4 = Entry(tela, width=50, font="Arial, 20")
    presenc_esp4.place(x=10, y=25)

    bt_salva = Button(tela, text="Salvar", bg="blue", fg="white", font="Arial, 15", command=salvar_presenc_esp4)
    bt_salva.place(x=600, y=60)

    tela.mainloop()


def salvar_presenc_esp4():
    global presenc_esp4, lbl_presenc_al_esp4, tela
    presenc = presenc_esp4.get()
    note = int(presenc_esp4.get())
    tela.destroy()

    arquivo = open('bd_al_esp4.pck', 'rb')
    bd_al_esp4 = pickle.load(arquivo)
    arquivo.close()

    bd_al_esp4["presenc"] = presenc

    arquivo = open('bd_al_esp4.pck', 'wb')
    lbl_presenc_al_esp4["text"] = presenc
    pickle.dump(bd_al_esp4, arquivo)
    arquivo.close()


def nivelt_al_esp4():
    global nivelt_esp4, tela
    tela = Tk()
    tela.configure(bg="white")
    tela.geometry("775x100+50+100")
    tela.title("Entrada do Nivel de Turma do Aluno do aluno")

    nivelt_esp4 = Entry(tela, width=50, font="Arial, 20")
    nivelt_esp4.place(x=10, y=25)

    bt_salva = Button(tela, text="Salvar", bg="blue", fg="white", font="Arial, 15", command=salvar_nivelt_esp4)
    bt_salva.place(x=600, y=60)

    tela.mainloop()


def salvar_nivelt_esp4():
    global nivelt_esp4, lbl_nivelt_al_esp4, tela
    nivelt = nivelt_esp4.get()
    tela.destroy()

    arquivo = open('bd_al_esp4.pck', 'rb')
    bd_al_esp4 = pickle.load(arquivo)
    arquivo.close()

    bd_al_esp4["nivelt"] = nivelt
    arquivo = open('bd_al_esp4.pck', 'wb')
    pickle.dump(bd_al_esp4, arquivo)
    arquivo.close()

    lbl_nivelt_al_esp4["text"] = nivelt


#####################################################################
# fim parte do programa dedicada ao aluno 4 de espanhol
#####################################################################

#####################################################################
#####################################################################
#####################################################################



#####################################################################
# parte do programa dedicada ao aluno 5 de espanhol
#####################################################################

def nome_al_esp5():
    global nome_esp5, tela
    tela = Tk()
    tela.configure(bg="white")
    tela.geometry("775x100+50+100")
    tela.title("Entrada do nome do aluno")

    nome_esp5 = Entry(tela, width=50, font="Arial, 20")
    nome_esp5.place(x=10, y=25)

    bt_salva = Button(tela, text="Salvar", bg="blue", fg="white", font="Arial, 15", command=salvar_nome_esp5)
    bt_salva.place(x=600, y=60)

    tela.mainloop()


def salvar_nome_esp5():
    global nome_esp5, lbl_nome_al_esp5, tela
    nome = nome_esp5.get().title()
    tela.destroy()

    arquivo = open('bd_al_esp5.pck', 'rb')
    bd_al_esp5 = pickle.load(arquivo)
    arquivo.close()

    bd_al_esp5["nome"] = nome
    arquivo = open('bd_al_esp5.pck', 'wb')
    pickle.dump(bd_al_esp5, arquivo)
    arquivo.close()
    lbl_nome_al_esp5["text"] = nome


def nota_al_esp5():
    global nota_esp5, tela, lbl_msg_nota_al_esp5
    tela = Tk()
    tela.configure(bg="white")
    tela.geometry("775x100+50+100")
    tela.title("Entrada do nome do aluno")

    nota_esp5 = Entry(tela, width=50, font="Arial, 20")

    bt_salva = Button(tela, text="Salvar", bg="blue", fg="white", font="Arial, 15", command=salvar_nota_esp5)

    lbl_msg_nota_al_esp5 = Label(tela, text="Digite a nota do aluno(valor entre 0 e 10)", bg="green", fg="white",
                                 font="Arial, 15")

    nota_esp5.place(x=10, y=25)
    bt_salva.place(x=600, y=60)
    lbl_msg_nota_al_esp5.place(x=15, y=65)
    tela.mainloop()


def salvar_nota_esp5():
    global nota_esp5, lbl_nota_al_esp5, tela, lbl_nv_al_esp5, lbl_msg_nota_al_esp5
    note = int(nota_esp5.get())
    nota = nota_esp5.get()
    lbl = note // 2

    if note < 0 or note > 10:
        lbl_msg_nota_al_esp5["text"] = "ERRO! a nota do aluno deve ser um numero entre 0 e 10"
        lbl_msg_nota_al_esp5["bg"] = "red"
        raise Exception
    elif note >= 0 and note <= 10:
        tela.destroy()
        arquivo = open('bd_al_esp5.pck', 'rb')
        bd_al_esp5 = pickle.load(arquivo)
        arquivo.close()

        bd_al_esp5["nota"] = nota

        arquivo = open('bd_al_esp5.pck', 'wb')
        pickle.dump(bd_al_esp5, arquivo)
        arquivo.close()

        lbl_nota_al_esp5["text"] = str(nota)
        lbl_nv_al_esp5["text"] = str(lbl)


def presenc_al_esp5():
    global presenc_esp5, tela
    tela = Tk()
    tela.configure(bg="white")
    tela.geometry("775x100+50+100")
    tela.title("Entrada das presenças do aluno")

    presenc_esp5 = Entry(tela, width=50, font="Arial, 20")
    presenc_esp5.place(x=10, y=25)

    bt_salva = Button(tela, text="Salvar", bg="blue", fg="white", font="Arial, 15", command=salvar_presenc_esp5)
    bt_salva.place(x=600, y=60)

    tela.mainloop()


def salvar_presenc_esp5():
    global presenc_esp5, lbl_presenc_al_esp5, tela
    presenc = presenc_esp5.get()
    note = int(presenc_esp5.get())
    tela.destroy()

    arquivo = open('bd_al_esp5.pck', 'rb')
    bd_al_esp5 = pickle.load(arquivo)
    arquivo.close()

    bd_al_esp5["presenc"] = presenc

    arquivo = open('bd_al_esp5.pck', 'wb')
    lbl_presenc_al_esp5["text"] = presenc
    pickle.dump(bd_al_esp5, arquivo)
    arquivo.close()


def nivelt_al_esp5():
    global nivelt_esp5, tela
    tela = Tk()
    tela.configure(bg="white")
    tela.geometry("775x100+50+100")
    tela.title("Entrada do Nivel de Turma do Aluno do aluno")

    nivelt_esp5 = Entry(tela, width=50, font="Arial, 20")
    nivelt_esp5.place(x=10, y=25)

    bt_salva = Button(tela, text="Salvar", bg="blue", fg="white", font="Arial, 15", command=salvar_nivelt_esp5)
    bt_salva.place(x=600, y=60)

    tela.mainloop()


def salvar_nivelt_esp5():
    global nivelt_esp5, lbl_nivelt_al_esp5, tela
    nivelt = nivelt_esp5.get()
    tela.destroy()

    arquivo = open('bd_al_esp5.pck', 'rb')
    bd_al_esp5 = pickle.load(arquivo)
    arquivo.close()

    bd_al_esp5["nivelt"] = nivelt
    arquivo = open('bd_al_esp5.pck', 'wb')
    pickle.dump(bd_al_esp5, arquivo)
    arquivo.close()

    lbl_nivelt_al_esp5["text"] = nivelt


#####################################################################
# fim parte do programa dedicada ao aluno 5 de espanhol
#####################################################################

#####################################################################
#####################################################################
#####################################################################



#####################################################################
# parte do programa dedicada ao aluno 6 de espanhol
#####################################################################

def nome_al_esp6():
    global nome_esp6, tela
    tela = Tk()
    tela.configure(bg="white")
    tela.geometry("775x100+50+100")
    tela.title("Entrada do nome do aluno")

    nome_esp6 = Entry(tela, width=50, font="Arial, 20")
    nome_esp6.place(x=10, y=25)

    bt_salva = Button(tela, text="Salvar", bg="blue", fg="white", font="Arial, 15", command=salvar_nome_esp6)
    bt_salva.place(x=600, y=60)

    tela.mainloop()


def salvar_nome_esp6():
    global nome_esp6, lbl_nome_al_esp6, tela
    nome = nome_esp6.get().title()
    tela.destroy()

    arquivo = open('bd_al_esp6.pck', 'rb')
    bd_al_esp6 = pickle.load(arquivo)
    arquivo.close()

    bd_al_esp6["nome"] = nome
    arquivo = open('bd_al_esp6.pck', 'wb')
    pickle.dump(bd_al_esp6, arquivo)
    arquivo.close()
    lbl_nome_al_esp6["text"] = nome


def nota_al_esp6():
    global nota_esp6, tela, lbl_msg_nota_al_esp6
    tela = Tk()
    tela.configure(bg="white")
    tela.geometry("775x100+50+100")
    tela.title("Entrada do nome do aluno")

    nota_esp6 = Entry(tela, width=50, font="Arial, 20")

    bt_salva = Button(tela, text="Salvar", bg="blue", fg="white", font="Arial, 15", command=salvar_nota_esp6)

    lbl_msg_nota_al_esp6 = Label(tela, text="Digite a nota do aluno(valor entre 0 e 10)", bg="green", fg="white",
                                 font="Arial, 15")

    nota_esp6.place(x=10, y=25)
    bt_salva.place(x=600, y=60)
    lbl_msg_nota_al_esp6.place(x=15, y=65)
    tela.mainloop()


def salvar_nota_esp6():
    global nota_esp6, lbl_nota_al_esp6, tela, lbl_nv_al_esp6, lbl_msg_nota_al_esp6
    note = int(nota_esp6.get())
    nota = nota_esp6.get()
    lbl = note // 2

    if note < 0 or note > 10:
        lbl_msg_nota_al_esp6["text"] = "ERRO! a nota do aluno deve ser um numero entre 0 e 10"
        lbl_msg_nota_al_esp6["bg"] = "red"
        raise Exception
    elif note >= 0 and note <= 10:
        tela.destroy()
        arquivo = open('bd_al_esp6.pck', 'rb')
        bd_al_esp6 = pickle.load(arquivo)
        arquivo.close()

        bd_al_esp6["nota"] = nota

        arquivo = open('bd_al_esp6.pck', 'wb')
        pickle.dump(bd_al_esp6, arquivo)
        arquivo.close()

        lbl_nota_al_esp6["text"] = str(nota)
        lbl_nv_al_esp6["text"] = str(lbl)


def presenc_al_esp6():
    global presenc_esp6, tela
    tela = Tk()
    tela.configure(bg="white")
    tela.geometry("775x100+50+100")
    tela.title("Entrada das presenças do aluno")

    presenc_esp6 = Entry(tela, width=50, font="Arial, 20")
    presenc_esp6.place(x=10, y=25)

    bt_salva = Button(tela, text="Salvar", bg="blue", fg="white", font="Arial, 15", command=salvar_presenc_esp6)
    bt_salva.place(x=600, y=60)

    tela.mainloop()


def salvar_presenc_esp6():
    global presenc_esp6, lbl_presenc_al_esp6, tela
    presenc = presenc_esp6.get()
    note = int(presenc_esp6.get())
    tela.destroy()

    arquivo = open('bd_al_esp6.pck', 'rb')
    bd_al_esp6 = pickle.load(arquivo)
    arquivo.close()

    bd_al_esp6["presenc"] = presenc

    arquivo = open('bd_al_esp6.pck', 'wb')
    lbl_presenc_al_esp6["text"] = presenc
    pickle.dump(bd_al_esp6, arquivo)
    arquivo.close()


def nivelt_al_esp6():
    global nivelt_esp6, tela
    tela = Tk()
    tela.configure(bg="white")
    tela.geometry("775x100+50+100")
    tela.title("Entrada do Nivel de Turma do Aluno do aluno")

    nivelt_esp6 = Entry(tela, width=50, font="Arial, 20")
    nivelt_esp6.place(x=10, y=25)

    bt_salva = Button(tela, text="Salvar", bg="blue", fg="white", font="Arial, 15", command=salvar_nivelt_esp6)
    bt_salva.place(x=600, y=60)

    tela.mainloop()


def salvar_nivelt_esp6():
    global nivelt_esp6, lbl_nivelt_al_esp6, tela
    nivelt = nivelt_esp6.get()
    tela.destroy()

    arquivo = open('bd_al_esp6.pck', 'rb')
    bd_al_esp6 = pickle.load(arquivo)
    arquivo.close()

    bd_al_esp6["nivelt"] = nivelt
    arquivo = open('bd_al_esp6.pck', 'wb')
    pickle.dump(bd_al_esp6, arquivo)
    arquivo.close()

    lbl_nivelt_al_esp6["text"] = nivelt


#####################################################################
# fim parte do programa dedicada ao aluno 6 de espanhol
#####################################################################

#####################################################################
#####################################################################
#####################################################################



#####################################################################
# parte do programa dedicada ao aluno 7 de espanhol
#####################################################################

def nome_al_esp7():
    global nome_esp7, tela
    tela = Tk()
    tela.configure(bg="white")
    tela.geometry("775x100+50+100")
    tela.title("Entrada do nome do aluno")

    nome_esp7 = Entry(tela, width=50, font="Arial, 20")
    nome_esp7.place(x=10, y=25)

    bt_salva = Button(tela, text="Salvar", bg="blue", fg="white", font="Arial, 15", command=salvar_nome_esp7)
    bt_salva.place(x=600, y=60)

    tela.mainloop()


def salvar_nome_esp7():
    global nome_esp7, lbl_nome_al_esp7, tela
    nome = nome_esp7.get().title()
    tela.destroy()

    arquivo = open('bd_al_esp7.pck', 'rb')
    bd_al_esp7 = pickle.load(arquivo)
    arquivo.close()

    bd_al_esp7["nome"] = nome
    arquivo = open('bd_al_esp7.pck', 'wb')
    pickle.dump(bd_al_esp7, arquivo)
    arquivo.close()
    lbl_nome_al_esp7["text"] = nome


def nota_al_esp7():
    global nota_esp7, tela, lbl_msg_nota_al_esp7
    tela = Tk()
    tela.configure(bg="white")
    tela.geometry("775x100+50+100")
    tela.title("Entrada do nome do aluno")

    nota_esp7 = Entry(tela, width=50, font="Arial, 20")

    bt_salva = Button(tela, text="Salvar", bg="blue", fg="white", font="Arial, 15", command=salvar_nota_esp7)

    lbl_msg_nota_al_esp7 = Label(tela, text="Digite a nota do aluno(valor entre 0 e 10)", bg="green", fg="white",
                                 font="Arial, 15")

    nota_esp7.place(x=10, y=25)
    bt_salva.place(x=600, y=60)
    lbl_msg_nota_al_esp7.place(x=15, y=65)
    tela.mainloop()


def salvar_nota_esp7():
    global nota_esp7, lbl_nota_al_esp7, tela, lbl_nv_al_esp7, lbl_msg_nota_al_esp7
    note = int(nota_esp7.get())
    nota = nota_esp7.get()
    lbl = note // 2

    if note < 0 or note > 10:
        lbl_msg_nota_al_esp7["text"] = "ERRO! a nota do aluno deve ser um numero entre 0 e 10"
        lbl_msg_nota_al_esp7["bg"] = "red"
        raise Exception
    elif note >= 0 and note <= 10:
        tela.destroy()
        arquivo = open('bd_al_esp7.pck', 'rb')
        bd_al_esp7 = pickle.load(arquivo)
        arquivo.close()

        bd_al_esp7["nota"] = nota

        arquivo = open('bd_al_esp7.pck', 'wb')
        pickle.dump(bd_al_esp7, arquivo)
        arquivo.close()

        lbl_nota_al_esp7["text"] = str(nota)
        lbl_nv_al_esp7["text"] = str(lbl)


def presenc_al_esp7():
    global presenc_esp7, tela
    tela = Tk()
    tela.configure(bg="white")
    tela.geometry("775x100+50+100")
    tela.title("Entrada das presenças do aluno")

    presenc_esp7 = Entry(tela, width=50, font="Arial, 20")
    presenc_esp7.place(x=10, y=25)

    bt_salva = Button(tela, text="Salvar", bg="blue", fg="white", font="Arial, 15", command=salvar_presenc_esp7)
    bt_salva.place(x=600, y=60)

    tela.mainloop()


def salvar_presenc_esp7():
    global presenc_esp7, lbl_presenc_al_esp7, tela
    presenc = presenc_esp7.get()
    note = int(presenc_esp7.get())
    tela.destroy()

    arquivo = open('bd_al_esp7.pck', 'rb')
    bd_al_esp7 = pickle.load(arquivo)
    arquivo.close()

    bd_al_esp7["presenc"] = presenc

    arquivo = open('bd_al_esp7.pck', 'wb')
    lbl_presenc_al_esp7["text"] = presenc
    pickle.dump(bd_al_esp7, arquivo)
    arquivo.close()


def nivelt_al_esp7():
    global nivelt_esp7, tela
    tela = Tk()
    tela.configure(bg="white")
    tela.geometry("775x100+50+100")
    tela.title("Entrada do Nivel de Turma do Aluno do aluno")

    nivelt_esp7 = Entry(tela, width=50, font="Arial, 20")
    nivelt_esp7.place(x=10, y=25)

    bt_salva = Button(tela, text="Salvar", bg="blue", fg="white", font="Arial, 15", command=salvar_nivelt_esp7)
    bt_salva.place(x=600, y=60)

    tela.mainloop()


def salvar_nivelt_esp7():
    global nivelt_esp7, lbl_nivelt_al_esp7, tela
    nivelt = nivelt_esp7.get()
    tela.destroy()

    arquivo = open('bd_al_esp7.pck', 'rb')
    bd_al_esp7 = pickle.load(arquivo)
    arquivo.close()

    bd_al_esp7["nivelt"] = nivelt
    arquivo = open('bd_al_esp7.pck', 'wb')
    pickle.dump(bd_al_esp7, arquivo)
    arquivo.close()

    lbl_nivelt_al_esp7["text"] = nivelt


#####################################################################
# fim parte do programa dedicada ao aluno 7 de espanhol
#####################################################################

#####################################################################
#####################################################################
#####################################################################



#####################################################################
# parte do programa dedicada ao aluno 8 de espanhol
#####################################################################

def nome_al_esp8():
    global nome_esp8, tela
    tela = Tk()
    tela.configure(bg="white")
    tela.geometry("775x100+50+100")
    tela.title("Entrada do nome do aluno")

    nome_esp8 = Entry(tela, width=50, font="Arial, 20")
    nome_esp8.place(x=10, y=25)

    bt_salva = Button(tela, text="Salvar", bg="blue", fg="white", font="Arial, 15", command=salvar_nome_esp8)
    bt_salva.place(x=600, y=60)

    tela.mainloop()


def salvar_nome_esp8():
    global nome_esp8, lbl_nome_al_esp8, tela
    nome = nome_esp8.get().title()
    tela.destroy()

    arquivo = open('bd_al_esp8.pck', 'rb')
    bd_al_esp8 = pickle.load(arquivo)
    arquivo.close()

    bd_al_esp8["nome"] = nome
    arquivo = open('bd_al_esp8.pck', 'wb')
    pickle.dump(bd_al_esp8, arquivo)
    arquivo.close()
    lbl_nome_al_esp8["text"] = nome


def nota_al_esp8():
    global nota_esp8, tela, lbl_msg_nota_al_esp8
    tela = Tk()
    tela.configure(bg="white")
    tela.geometry("775x100+50+100")
    tela.title("Entrada do nome do aluno")

    nota_esp8 = Entry(tela, width=50, font="Arial, 20")

    bt_salva = Button(tela, text="Salvar", bg="blue", fg="white", font="Arial, 15", command=salvar_nota_esp8)

    lbl_msg_nota_al_esp8 = Label(tela, text="Digite a nota do aluno(valor entre 0 e 10)", bg="green", fg="white",
                                 font="Arial, 15")

    nota_esp8.place(x=10, y=25)
    bt_salva.place(x=600, y=60)
    lbl_msg_nota_al_esp8.place(x=15, y=65)
    tela.mainloop()


def salvar_nota_esp8():
    global nota_esp8, lbl_nota_al_esp8, tela, lbl_nv_al_esp8, lbl_msg_nota_al_esp8
    note = int(nota_esp8.get())
    nota = nota_esp8.get()
    lbl = note // 2

    if note < 0 or note > 10:
        lbl_msg_nota_al_esp8["text"] = "ERRO! a nota do aluno deve ser um numero entre 0 e 10"
        lbl_msg_nota_al_esp8["bg"] = "red"
        raise Exception
    elif note >= 0 and note <= 10:
        tela.destroy()
        arquivo = open('bd_al_esp8.pck', 'rb')
        bd_al_esp8 = pickle.load(arquivo)
        arquivo.close()

        bd_al_esp8["nota"] = nota

        arquivo = open('bd_al_esp8.pck', 'wb')
        pickle.dump(bd_al_esp8, arquivo)
        arquivo.close()

        lbl_nota_al_esp8["text"] = str(nota)
        lbl_nv_al_esp8["text"] = str(lbl)


def presenc_al_esp8():
    global presenc_esp8, tela
    tela = Tk()
    tela.configure(bg="white")
    tela.geometry("775x100+50+100")
    tela.title("Entrada das presenças do aluno")

    presenc_esp8 = Entry(tela, width=50, font="Arial, 20")
    presenc_esp8.place(x=10, y=25)

    bt_salva = Button(tela, text="Salvar", bg="blue", fg="white", font="Arial, 15", command=salvar_presenc_esp8)
    bt_salva.place(x=600, y=60)

    tela.mainloop()


def salvar_presenc_esp8():
    global presenc_esp8, lbl_presenc_al_esp8, tela
    presenc = presenc_esp8.get()
    note = int(presenc_esp8.get())
    tela.destroy()

    arquivo = open('bd_al_esp8.pck', 'rb')
    bd_al_esp8 = pickle.load(arquivo)
    arquivo.close()

    bd_al_esp8["presenc"] = presenc

    arquivo = open('bd_al_esp8.pck', 'wb')
    lbl_presenc_al_esp8["text"] = presenc
    pickle.dump(bd_al_esp8, arquivo)
    arquivo.close()


def nivelt_al_esp8():
    global nivelt_esp8, tela
    tela = Tk()
    tela.configure(bg="white")
    tela.geometry("775x100+50+100")
    tela.title("Entrada do Nivel de Turma do Aluno do aluno")

    nivelt_esp8 = Entry(tela, width=50, font="Arial, 20")
    nivelt_esp8.place(x=10, y=25)

    bt_salva = Button(tela, text="Salvar", bg="blue", fg="white", font="Arial, 15", command=salvar_nivelt_esp8)
    bt_salva.place(x=600, y=60)

    tela.mainloop()


def salvar_nivelt_esp8():
    global nivelt_esp8, lbl_nivelt_al_esp8, tela
    nivelt = nivelt_esp8.get()
    tela.destroy()

    arquivo = open('bd_al_esp8.pck', 'rb')
    bd_al_esp8 = pickle.load(arquivo)
    arquivo.close()

    bd_al_esp8["nivelt"] = nivelt
    arquivo = open('bd_al_esp8.pck', 'wb')
    pickle.dump(bd_al_esp8, arquivo)
    arquivo.close()

    lbl_nivelt_al_esp8["text"] = nivelt


#####################################################################
# fim parte do programa dedicada ao aluno 8 de espanhol
#####################################################################

#####################################################################
#####################################################################
#####################################################################



#####################################################################
# parte do programa dedicada ao aluno 9 de espanhol
#####################################################################

def nome_al_esp9():
    global nome_esp9, tela
    tela = Tk()
    tela.configure(bg="white")
    tela.geometry("775x100+50+100")
    tela.title("Entrada do nome do aluno")

    nome_esp9 = Entry(tela, width=50, font="Arial, 20")
    nome_esp9.place(x=10, y=25)

    bt_salva = Button(tela, text="Salvar", bg="blue", fg="white", font="Arial, 15", command=salvar_nome_esp9)
    bt_salva.place(x=600, y=60)

    tela.mainloop()


def salvar_nome_esp9():
    global nome_esp9, lbl_nome_al_esp9, tela
    nome = nome_esp9.get().title()
    tela.destroy()

    arquivo = open('bd_al_esp9.pck', 'rb')
    bd_al_esp9 = pickle.load(arquivo)
    arquivo.close()

    bd_al_esp9["nome"] = nome
    arquivo = open('bd_al_esp9.pck', 'wb')
    pickle.dump(bd_al_esp9, arquivo)
    arquivo.close()
    lbl_nome_al_esp9["text"] = nome


def nota_al_esp9():
    global nota_esp9, tela, lbl_msg_nota_al_esp9
    tela = Tk()
    tela.configure(bg="white")
    tela.geometry("775x100+50+100")
    tela.title("Entrada do nome do aluno")

    nota_esp9 = Entry(tela, width=50, font="Arial, 20")

    bt_salva = Button(tela, text="Salvar", bg="blue", fg="white", font="Arial, 15", command=salvar_nota_esp9)

    lbl_msg_nota_al_esp9 = Label(tela, text="Digite a nota do aluno(valor entre 0 e 10)", bg="green", fg="white",
                                 font="Arial, 15")

    nota_esp9.place(x=10, y=25)
    bt_salva.place(x=600, y=60)
    lbl_msg_nota_al_esp9.place(x=15, y=65)
    tela.mainloop()


def salvar_nota_esp9():
    global nota_esp9, lbl_nota_al_esp9, tela, lbl_nv_al_esp9, lbl_msg_nota_al_esp9
    note = int(nota_esp9.get())
    nota = nota_esp9.get()
    lbl = note // 2

    if note < 0 or note > 10:
        lbl_msg_nota_al_esp9["text"] = "ERRO! a nota do aluno deve ser um numero entre 0 e 10"
        lbl_msg_nota_al_esp9["bg"] = "red"
        raise Exception
    elif note >= 0 and note <= 10:
        tela.destroy()
        arquivo = open('bd_al_esp9.pck', 'rb')
        bd_al_esp9 = pickle.load(arquivo)
        arquivo.close()

        bd_al_esp9["nota"] = nota

        arquivo = open('bd_al_esp9.pck', 'wb')
        pickle.dump(bd_al_esp9, arquivo)
        arquivo.close()

        lbl_nota_al_esp9["text"] = str(nota)
        lbl_nv_al_esp9["text"] = str(lbl)


def presenc_al_esp9():
    global presenc_esp9, tela
    tela = Tk()
    tela.configure(bg="white")
    tela.geometry("775x100+50+100")
    tela.title("Entrada das presenças do aluno")

    presenc_esp9 = Entry(tela, width=50, font="Arial, 20")
    presenc_esp9.place(x=10, y=25)

    bt_salva = Button(tela, text="Salvar", bg="blue", fg="white", font="Arial, 15", command=salvar_presenc_esp9)
    bt_salva.place(x=600, y=60)

    tela.mainloop()


def salvar_presenc_esp9():
    global presenc_esp9, lbl_presenc_al_esp9, tela
    presenc = presenc_esp9.get()
    note = int(presenc_esp9.get())
    tela.destroy()

    arquivo = open('bd_al_esp9.pck', 'rb')
    bd_al_esp9 = pickle.load(arquivo)
    arquivo.close()

    bd_al_esp9["presenc"] = presenc

    arquivo = open('bd_al_esp9.pck', 'wb')
    lbl_presenc_al_esp9["text"] = presenc
    pickle.dump(bd_al_esp9, arquivo)
    arquivo.close()


def nivelt_al_esp9():
    global nivelt_esp9, tela
    tela = Tk()
    tela.configure(bg="white")
    tela.geometry("775x100+50+100")
    tela.title("Entrada do Nivel de Turma do Aluno do aluno")

    nivelt_esp9 = Entry(tela, width=50, font="Arial, 20")
    nivelt_esp9.place(x=10, y=25)

    bt_salva = Button(tela, text="Salvar", bg="blue", fg="white", font="Arial, 15", command=salvar_nivelt_esp9)
    bt_salva.place(x=600, y=60)

    tela.mainloop()


def salvar_nivelt_esp9():
    global nivelt_esp9, lbl_nivelt_al_esp9, tela
    nivelt = nivelt_esp9.get()
    tela.destroy()

    arquivo = open('bd_al_esp9.pck', 'rb')
    bd_al_esp9 = pickle.load(arquivo)
    arquivo.close()

    bd_al_esp9["nivelt"] = nivelt
    arquivo = open('bd_al_esp9.pck', 'wb')
    pickle.dump(bd_al_esp9, arquivo)
    arquivo.close()

    lbl_nivelt_al_esp9["text"] = nivelt


#####################################################################
# fim parte do programa dedicada ao aluno 9 de espanhol
#####################################################################

#####################################################################
#####################################################################
#####################################################################



#####################################################################
# parte do programa dedicada ao aluno 10 de espanhol
#####################################################################

def nome_al_esp10():
    global nome_esp10, tela
    tela = Tk()
    tela.configure(bg="white")
    tela.geometry("775x100+50+100")
    tela.title("Entrada do nome do aluno")

    nome_esp10 = Entry(tela, width=50, font="Arial, 20")
    nome_esp10.place(x=10, y=25)

    bt_salva = Button(tela, text="Salvar", bg="blue", fg="white", font="Arial, 15", command=salvar_nome_esp10)
    bt_salva.place(x=600, y=60)

    tela.mainloop()


def salvar_nome_esp10():
    global nome_esp10, lbl_nome_al_esp10, tela
    nome = nome_esp10.get().title()
    lbl_nome_al_esp10["text"] = nome
    tela.destroy()

    arquivo = open('bd_al_esp10.pck', 'rb')
    bd_al_esp10 = pickle.load(arquivo)
    arquivo.close()

    bd_al_esp10["nome"] = nome
    arquivo = open('bd_al_esp10.pck', 'wb')
    pickle.dump(bd_al_esp10, arquivo)
    arquivo.close()


def nota_al_esp10():
    global nota_esp10, tela, lbl_msg_nota_al_esp10
    tela = Tk()
    tela.configure(bg="white")
    tela.geometry("775x100+50+100")
    tela.title("Entrada do nome do aluno")

    nota_esp10 = Entry(tela, width=50, font="Arial, 20")

    bt_salva = Button(tela, text="Salvar", bg="blue", fg="white", font="Arial, 15", command=salvar_nota_esp10)

    lbl_msg_nota_al_esp10 = Label(tela, text="Digite a nota do aluno(valor entre 0 e 10)", bg="green", fg="white",
                                  font="Arial, 15")

    nota_esp10.place(x=10, y=25)
    bt_salva.place(x=600, y=60)
    lbl_msg_nota_al_esp10.place(x=15, y=65)
    tela.mainloop()


def salvar_nota_esp10():
    global nota_esp10, lbl_nota_al_esp10, tela, lbl_nv_al_esp10, lbl_msg_nota_al_esp10
    note = int(nota_esp10.get())
    nota = nota_esp10.get()
    lbl = note // 2

    if note < 0 or note > 10:
        lbl_msg_nota_al_esp10["text"] = "ERRO! a nota do aluno deve ser um numero entre 0 e 10"
        lbl_msg_nota_al_esp10["bg"] = "red"
        raise Exception
    elif note >= 0 and note <= 10:
        tela.destroy()
        arquivo = open('bd_al_esp10.pck', 'rb')
        bd_al_esp10 = pickle.load(arquivo)
        arquivo.close()

        bd_al_esp10["nota"] = nota

        arquivo = open('bd_al_esp10.pck', 'wb')
        pickle.dump(bd_al_esp10, arquivo)
        arquivo.close()

        lbl_nota_al_esp10["text"] = str(nota)
        lbl_nv_al_esp10["text"] = str(lbl)


def presenc_al_esp10():
    global presenc_esp10, tela
    tela = Tk()
    tela.configure(bg="white")
    tela.geometry("775x100+50+100")
    tela.title("Entrada das presenças do aluno")

    presenc_esp10 = Entry(tela, width=50, font="Arial, 20")
    presenc_esp10.place(x=10, y=25)

    bt_salva = Button(tela, text="Salvar", bg="blue", fg="white", font="Arial, 15", command=salvar_presenc_esp10)
    bt_salva.place(x=600, y=60)

    tela.mainloop()


def salvar_presenc_esp10():
    global presenc_esp10, lbl_presenc_al_esp10, tela
    presenc = presenc_esp10.get()
    note = int(presenc_esp10.get())
    tela.destroy()

    arquivo = open('bd_al_esp10.pck', 'rb')
    bd_al_esp10 = pickle.load(arquivo)
    arquivo.close()

    bd_al_esp10["presenc"] = presenc

    arquivo = open('bd_al_esp10.pck', 'wb')
    lbl_presenc_al_esp10["text"] = presenc
    pickle.dump(bd_al_esp10, arquivo)
    arquivo.close()


def nivelt_al_esp10():
    global nivelt_esp10, tela
    tela = Tk()
    tela.configure(bg="white")
    tela.geometry("775x100+50+100")
    tela.title("Entrada do Nivel de Turma do Aluno do aluno")

    nivelt_esp10 = Entry(tela, width=50, font="Arial, 20")
    nivelt_esp10.place(x=10, y=25)

    bt_salva = Button(tela, text="Salvar", bg="blue", fg="white", font="Arial, 15", command=salvar_nivelt_esp10)
    bt_salva.place(x=600, y=60)

    tela.mainloop()


def salvar_nivelt_esp10():
    global nivelt_esp10, lbl_nivelt_al_esp10, tela
    nivelt = nivelt_esp10.get()
    tela.destroy()

    arquivo = open('bd_al_esp10.pck', 'rb')
    bd_al_esp10 = pickle.load(arquivo)
    arquivo.close()

    bd_al_esp10["nivelt"] = nivelt
    arquivo = open('bd_al_esp10.pck', 'wb')
    pickle.dump(bd_al_esp10, arquivo)
    arquivo.close()

    lbl_nivelt_al_esp10["text"] = nivelt

#####################################################################
# fim parte do programa dedicada ao aluno 10 de espanhol
#####################################################################

#####################################################################
#####################################################################
#####################################################################
