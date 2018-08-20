import kivy
kivy.require("1.9.1")
import sqlite3
from kivy.app import App
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput

class Login(App):
    def build(self):
        pass



    def entrar(self):
        conn = sqlite3.connect("usuario.db")
        cursor = conn.execute("SELECT * FROM usuarios")
        usuarios = cursor.fetchall()
        conn.close()

        for pessoa in usuarios:
            if pessoa[0] == "a":
                print("existe")




Login().run()