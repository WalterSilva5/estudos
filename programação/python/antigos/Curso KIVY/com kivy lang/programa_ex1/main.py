from kivy.app import App
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.floatlayout import FloatLayout

class RootWidget(FloatLayout):
    pass

class ProgramaApp(App):
    def build(self):
        return RootWidget()

ProgramaApp().run()