a função import adiciona o simbolo do modulo importado a tabela de simbolos local


ex codigo de modulo ferramentas:

a = 10
b = 20

def soma():
    return a+b



import ferramentas:
    os simbolos do modulo ferramentas ficam disponiveis atraves da forma

    ferramentas.simbolo
    ou ferramentas.simbolo()
ex:
    num = ferramentas.a
    e
    num2 = ferramentas.soma()

from ferramentas import *
    todos os simbolos ficam assessiveis diretamente
    ex:
    num = a
    e
    num2 = soma()
