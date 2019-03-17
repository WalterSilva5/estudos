from kivy.app import App
from kivy.uix.button import Button

#funcao que o botao executa
def click():
    print("o botao foi clicado")

def build():
    #criamos um botao
    bt = Button(text = "clique Aqui")

    #definimos o evento do botao bt
    bt.on_press=click

    return bt

janela = App()
janela.build = build
janela.run()
