from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.stacklayout import StackLayout
from kivy.uix.label import Label

#stack alinhamento em forma de pilha
class Tela1(StackLayout):
    pass

class Janelaex4App(App):
    def build(self):
        return Tela1()

janela = Janelaex4App()
janela.run()
