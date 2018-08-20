from kivy.app import App
from kivy.uix.label import Label


class HelloApp(App):
    #o codigo do arquivo hello.kv sera executado  aqui
    pass
    """
    o kivy sempre ira procurar o arquivo cujo nome seja o nome da classe
    em minusculo e sem o final App no nome

    ex essa classe se chama Hello
    entao ele vai procurar o arquivo hello.kv
    e vai executar o codigo dele nessa classe 
    """

HelloApp().run()
