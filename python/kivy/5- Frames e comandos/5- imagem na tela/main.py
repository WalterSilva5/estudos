from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.image import Image
class Tela1(FloatLayout):
    pass

class JanelaApp(App):
    def build(self):
        return Tela1()

janela = JanelaApp()
janela.run()
