from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.floatlayout import FloatLayout

class Tela1(FloatLayout):
    pass

class Janelaex2App(App):
    def build(self):
        return Tela1()

Janelaex2App().run()
