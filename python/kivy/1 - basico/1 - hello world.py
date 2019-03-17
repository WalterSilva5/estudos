#importamos a classe App do kivy
from kiv.app import App
#importamos o widget label do kivy
from kivy.uix.label import Label

#definimos um metodo chamado build para ser executado ao executar o app
def build():
    return Label(text="hello world")

#criamos um novo app chamado hello_world
hello_world = App()
#definimos que o metodo build vai sobrescrever o metodo hello_world
hello_world.build = build
#executamos o app hello_world
hello_world.run()
