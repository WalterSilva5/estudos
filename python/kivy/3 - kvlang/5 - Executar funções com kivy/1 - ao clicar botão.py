from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout

#esse programa remove um container e o subistitui por outro

class Tela1(BoxLayout):
    def on_press_executar_tela1(self):
        janela.root_window.remove_widget(janela.root_window)
        janela.root_window.add_widget(Tela2())

class Tela2(BoxLayout):
    def on_press_executar_tela2(self):
        janela.root_window.remove_widget(janela.root_window)
        janela.root_window.add_widget(Tela1())

class Executar1App(App):
    def build(self):
        return Tela1()

janela = Executar1App()
janela.run()
