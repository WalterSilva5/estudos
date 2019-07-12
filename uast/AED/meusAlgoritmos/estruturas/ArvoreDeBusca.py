"""
Balanceamento

Soma de todos os elementos da árvore

Altura da árvore

Níveis da árvore

Elementos de cada nível

Add

Buscar elemento

Remover

GetMax

GetMin

Antecessor

Predecessor

Total de elementos de um no (no caso, se não especificar o no, é da árvore)

Retornar nível do elemento
"""


class ArvoreBuscaBinaria:
    def __init__(self):
        self.__raiz

    class No:
        pass

    def inserir(self, valor):
        pass
    def minimo(self, atual=None):
        pass
    def maximo(self, atual=None):
        pass
    def buscar(self, valor):
        pass

    def apagar(self, valor):
        pass

    def recortar(self, sera_removido, sera_recortado):
        pass


    def sucessor(self, valor):
        pass

    def predecessor(self, valor):
        pass


    def listar(self):
        pass


arvore = ArvoreBuscaBinaria()

arvore.inserir(15)
arvore.inserir(6)
arvore.inserir(3)
arvore.inserir(2)
arvore.inserir(4)
arvore.inserir(7)
arvore.inserir(13)
arvore.inserir(9)
arvore.inserir(18)
arvore.inserir(17)
arvore.inserir(20)

print('O maior elemento da árvore é: {}'.format(arvore.maximo()))
print('O menor elemento da árvore é: {}'.format(arvore.minimo()))

print(arvore.apagar(15))
print(arvore.listar())
