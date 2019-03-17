from kivy.app import App
from kivy.uix.label import Label

#extendemos a classe App
class MeuPrograma(App):
    #sobreescrevemos o metodo build da classe App
    def build(self):
        return Label(text="Ola Mundo!")

#instanciamos a classe MeuPrograma
janela = MeuPrograma()
#executamos o metodo run do objeto janela
janela.run()
