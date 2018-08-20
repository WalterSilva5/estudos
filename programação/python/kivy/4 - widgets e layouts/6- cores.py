from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.label import Label

#stack alinhamento em forma de pilha
class Tela1(FloatLayout):
    pass

class Janelaex6App(App):
    def build(self):
        return Tela1()

janela = Janelaex6App()
janela.run()
