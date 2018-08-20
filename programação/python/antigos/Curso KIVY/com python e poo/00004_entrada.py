from kivy.app import App
from kivy.uix.textinput import TextInput

def build():
    return TextInput(text="Tela")

tela = App()
tela.build = build
tela.run()