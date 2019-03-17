from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.label import Label
from kivy.utils import get_color_from_hex

#importamos o modulo window
from kivy.core.window import Window

#modamos a cor padrão de fundo da janela
Window.clearcolor = get_color_from_hex("#000000")

class Tela1(FloatLayout):
    def atribui_texto(self):
        self.ids.label_texto.text = self.ids.entrada_de_texto.text

class Janelaex8App(App):
    def build(self):
        return Tela1()

janela = Janelaex8App()
janela.run()
