from kivy.app import App
from kivy.uix.label import Label

def build():
    return Label(text="Mensagem",font_size = 50)

tela = App()
tela.build = build

tela.run()