from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout

class Tela1(BoxLayout):
    pass

class Tela2(BoxLayout):
    pass

class Janelaex3App(App):
    def build(self):
        return Tela1()

janela = Janelaex3App()
janela.run()
