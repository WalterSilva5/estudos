import kivy
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button

class Tela1(BoxLayout):
    def pressionou_botao(self):
        #aqui manipulamos atraves dos ids definidos no arquivo kv
        self.ids.teste.text = "Texto Mudou"
        self.ids.teste.color= (0, 1, 0, 1)

class TelaApp(App):
    def build(self):
        return Tela1()

tela = TelaApp()
tela.run()
