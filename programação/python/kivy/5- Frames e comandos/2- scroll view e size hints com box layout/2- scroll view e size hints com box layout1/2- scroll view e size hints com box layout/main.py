from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.scrollview import ScrollView
from kivy.uix.button import Button
from kivy.uix.label import Label


class Tela(ScrollView):
    pass

class JanelaApp(App):
    def build(self):
        return Tela()

janela = JanelaApp()
janela.run()
