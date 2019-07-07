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

    