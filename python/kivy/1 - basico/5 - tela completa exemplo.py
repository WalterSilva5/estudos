from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.uix.floatlayout import FloatLayout

def click():
    global texto
    texto+="clicado-"
    ed.text = texto


def build():
    layout = FloatLayout()
    global ed, texto
    texto=""
    ed = TextInput()
    #definimos as dimenções:
    ed.size_hint = None, None#zeramos as dimenções
    ed.height = 100
    ed.width = 600
    #definimos as posições
    ed.y = 500
    ed.x = 0

    bt = Button(text="clique")
    bt.on_press=click
    bt.size_hint = None, None
    bt.height = 100
    bt.width = 200
    bt.y = 400
    bt.x = 200
    #adicionamos os widgets ao layout
    layout.add_widget(ed)
    layout.add_widget(bt)

    #retornamos o layout
    return layout

janela =App()
janela.build = build
janela.run()
