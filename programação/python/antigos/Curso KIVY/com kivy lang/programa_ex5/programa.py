#coding: utf-8
import kivy
kivy.require("1.9.1")
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button

def funcSelf(x):
    print("funcself")
Button.funcSelf = funcSelf

class MinhaTela(BoxLayout):
    def funcRoot(self):
        print("funcroot")

class Janela(App):
    def funcApp(self):
        print("funcApp")


tela = Janela()
tela.run()