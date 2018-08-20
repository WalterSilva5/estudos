#coding: utf-8

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
FloatLayout:
    Button:
        size_hint: .1, .1
        pos_hint: {"x": 0, "top":1.}
        text: "A"
    Button:
        size_hint: .2, .2
        pos_hint: {"center_x": .5, "center_y": .5}
        text: "B"
    Button:
        size_hint: .1, .1
        pos_hint: {"y": 0 , "right": 1}
        text: "C"
    
    Button:
        size_hint: None, None
        pos_hint: {"center_y": .7}
        x: 150
        width: 200
        height: 100
        text: "Absoluto"

"""
glayout = Builder.load_string(kvcode)
janela.root_window.add_widget(glayout)