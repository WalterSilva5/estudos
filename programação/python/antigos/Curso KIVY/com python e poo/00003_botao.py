from kivy.app import App
from kivy.uix.button import Button

def build():
    bt = Button(text="Clique Aqui")
    bt.on_press=click
    return bt

def click():
    print("Clicado")

tela = App()
tela.build = build
tela.run()