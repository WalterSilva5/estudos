import kivy
kivy.require("1.9.1")
from kivy.app import App
from kivy.lang import Builder

#tamanho da fonte
"""kvcode = ""-"
Label: 
    font_size: 40
    text: "texto"
""-"

"""

#fonte usada"""

"""

kvcode = 
Label: 
    #negrito
    bold: True
    font_size: 40
    text: "texto"
    
"""

kvcode = """
Label: 
    
    #italico
    italic: True
    
    #negrito
    bold: True
    
    #cor
    color: .1, 1, .1, 1
    
    #desabilitar escurecer texto
    disabled: False
    
    font_size: 40
    text: "texto"
    
    #tags: [b]texto[/b] negrito
    #[i][/i]  [u][/u] [s][/s]
    #[size = 50]texto[/size]
    #[color = ff3333]texto[/color]
    #[sup]texto[/sup] --superior [sub]texto[/sub] -- infferior
    
    
    
"""
class Programa(App):
    def build(self):
        return Builder.load_string(kvcode)


Programa().run()