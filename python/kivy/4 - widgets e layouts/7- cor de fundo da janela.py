from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.label import Label
from kivy.utils import get_color_from_hex

#importamos o modulo window
from kivy.core.window import Window

#modamos a cor padrão de fundo da janela
Window.clearcolor = get_color_from_hex("#a0a0a0")
class Tela1(FloatLayout):
    pass

class Janelaex7App(App):
    def build(self):
        return Tela1()

janela = Janelaex7App()
janela.run()
