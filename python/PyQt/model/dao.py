import sqlite3

class DAO():
    def listarTodos(parametro):
        conn = sqlite3.connect('model/SQL/bancoDeDados.db')
        cursor = conn.cursor()
        lista = cursor.execute("SELECT * FROM '{}'".format(parametro)).fetchall()
        conn.close()
        return lista

    def buscarFuncionario(nome, senha)  