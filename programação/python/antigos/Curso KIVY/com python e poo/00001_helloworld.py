from kivy.app import App
from kivy.uix.label import  Label

class Programa(App):
    def build(self):
        return Label(text="Hello")


Programa().run()