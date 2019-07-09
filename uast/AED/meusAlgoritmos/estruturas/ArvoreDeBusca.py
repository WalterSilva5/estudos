class Arvore():
    def __init__(self):
        self.__raiz = None

    class No:
        def __init__(self, valor):
            self.pai = None
            self.direita = None
            self.esquerda = None
            self.valor = valor

        def __str__(self):
            return str(self.valor)
        def __repr__(self):
            return self.__str__()

    def inserir(self, valor):
        pai

ar = Arvore()
ar.inserir(4)
ar.inserir(1)
ar.inserir(3)
ar.inserir(2)

print(ar.maximo())