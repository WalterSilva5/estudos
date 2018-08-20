from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.uix.floatlayout import FloatLayout

def click():
    print(ed.text)

def build():
    layout = FloatLayout()
    ed = TextInput(size_hint=(None, None), height=50, width=400, x=0, y=550, font_size=30)
    global ed
    bt = Button(text="Enviar", size_hint=(None, None), height=50, width=100, x=300, y=500)
    bt.on_press = click
    layout.add_widget(ed)
    layout.add_widget(bt)
    return layout

tela=App()
from kivy.core.window import Window
tela.title="Programa Inutil"
Window.size = 400,600
tela.build = build
tela.run()