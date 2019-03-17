from kivy.app import App
from kivy.uix.label import Label

def build():
    return Label(text = "ola", italic = True, font_size = 50)

    #ou:
    lb = Label()
    lb.text = "ola mundo"
    lb.italic = True
    lb.font_size = 50
    return lb
    
ola = App()
ola.build = build
ola.run()
