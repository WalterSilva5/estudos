# coding: utf-8
from kivy.app import App
from kivy.uix.button import Button
from kivy.interactive import InteractiveLauncher
from kivy.lang import Builder
from kivy.utils import get_color_from_hex
janela = None
glayout = None

class JanelaApp(App):
    pass

janela = JanelaApp()
ji = InteractiveLauncher(janela)
ji.run()

kvcode = """
#biblioteca que recebe hexadecimal para cor 
#: import C kivy.utils.get_color_from_hex
FloatLayout:
    Button:
        #com rgba
        #background_color: 5, .1, .1, 1
        #com hex
        background_color: C("#FFFFFF")
        background_normal: ""
        size_hint: .5, .5
        pos_hint: {"top": .75, "right": .75}
        text: "Clique"
        
"""
glayout = Builder.load_string(kvcode)
janela.root_window.add_widget(glayout)