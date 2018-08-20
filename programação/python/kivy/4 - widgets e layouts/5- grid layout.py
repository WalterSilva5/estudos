from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label

#stack alinhamento em forma de pilha
class Tela1(GridLayout):
    pass

class Janelaex5App(App):
    def build(self):
        return Tela1()

janela = Janelaex5App()
janela.run()
