from kivy.app import App
from kivy.uix.textinput import TextInput

def build():
    return TextInput()
    
janela = App()
janela.build = build
janela.run()
