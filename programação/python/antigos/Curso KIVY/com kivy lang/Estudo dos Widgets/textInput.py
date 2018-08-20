import kivy
kivy.require("1.9.1")
from kivy.app import App
from kivy.lang import Builder


kvcode = """
TextInput:
    size_hint: None, None
    size: 500, 100
    font_size: 30
    font_name: "arial"
    foreground_color: 1, 0, 1, 1
    background_color: 1, 1, .5, 1
    padding: 30
"""

class Programa(App):
    def build(self):
        return Builder.load_string(kvcode)

# var = Programa().text a variavel guarda o texto
#var.readonly = True / o texto fica não editavel
Programa().run()