import kivy

kivy.require("1.9.1")
from kivy.app import App
from kivy.lang import Builder


kvcode = """
Button:
    size_hint: None, None
    size: 500, 100
    font_size: 30
    font_name: "consola"
    italic: True
    color: 1, .3, .3 , 1 
    text: "Clique Aqui Para Iniciar"

"""
def click(bt):
    bt.text = "on Press"
def fim_click:
    bt.text = "on release"

bt.bind(on_press=click)
bt.bind(on_release=fim_click)

class Programa(App):
    def build(self):
        x = Builder.load_string(kvcode)
        return x

Programa().run()