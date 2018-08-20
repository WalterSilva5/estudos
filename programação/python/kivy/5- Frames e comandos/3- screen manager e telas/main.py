from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.boxlayout import BoxLayout

class Tela1(Screen):
    pass

class JanelaApp(App):
    def build(self):
        return Tela1()

janela = JanelaApp()
janela.run()
