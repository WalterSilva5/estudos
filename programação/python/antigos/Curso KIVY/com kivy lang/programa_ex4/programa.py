#coding: utf-8
import kivy
kivy.require("1.9.1")
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout

class MinhaTela(BoxLayout):
    def click(self):
        print("oi")
        self.ids.lb1.text = "Clicado1"
        self.ids.lb2.text = "Clicado2"


class janela(App):
    def build(self):
        pass

janela().run()