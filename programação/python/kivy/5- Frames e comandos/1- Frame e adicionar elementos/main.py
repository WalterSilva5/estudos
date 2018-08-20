from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.stacklayout import StackLayout

class Tela(FloatLayout):
    def adiciona_botao(self):
        self.ids.botoes.add_widget(Button(text= "bt", size_hint=(None, None),
                size=(100, 50)))

class JanelaApp(App):
    def build(self):
        return Tela()

janela = JanelaApp()
janela.run()
