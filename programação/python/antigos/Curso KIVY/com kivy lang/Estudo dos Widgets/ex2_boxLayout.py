# coding: utf-8

from kivy.app import App
from kivy.uix.button import Button
from kivy.interactive import InteractiveLauncher
from kivy.lang import Builder

janela = None
glayout = None


class JanelaApp(App):
    pass


janela = JanelaApp()
ji = InteractiveLauncher(janela)
ji.run()

kvcode = """
BoxLayout:
    orientation: "vertical"
    Button:
        size_hint: 1., 1.
        text: "A"

    Button:
        size_hint: 1., 1.
        text: "B"
        
    Button:
        size_hint: 1., 1.
        text: "C"


"""
glayout = Builder.load_string(kvcode)
janela.root_window.add_widget(glayout)