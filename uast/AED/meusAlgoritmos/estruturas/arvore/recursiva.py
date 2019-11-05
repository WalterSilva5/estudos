
class No:
    def __init__(self, valor):
        self.pai = None
        self.esquerda = None
        self.direita = None
        self.valor = valor

        def __str__(self):
            return str(self.valor)

        def __repr__(self):
            return self.__str__()


class ArvoreBuscaBinaria:
    def __init__(self):
        self.__raiz = None
        self.numeroDeFolhas = 0

    def add(self, valor):
        no = No(valor)
        if self.__raiz is None:
            self.__raiz = no
        else:
            self.addRec(self.__raiz, no)# começa pela raiz

    def addRec(self, atual, no):
        if no.valor > atual.valor:
            if atual.direita is None:
                atual.direita = no
            else:
                self.addRec(atual.direita, no) 
        elif no.valor < atual.valor:
            if atual.esquerda is None:
                atual.esquerda = no
            else:
                self.addRec(atual.esquerda, no)
            