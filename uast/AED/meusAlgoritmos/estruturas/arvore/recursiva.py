
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
        atual = self.__raiz
        if atual is None:
            self.__raiz = no
        else:
            self.addRec(self.__raiz, no, atual.pai)# começa pela raiz

    def addRec(self, atual, no, pai):
        no.pai = pai
        if no.valor > atual.valor:
            if atual.direita is None:
                atual.direita = no
            else:
                self.addRec(atual.direita, no, atual) 
        elif no.valor < atual.valor:
            if atual.esquerda is None:
                atual.esquerda = no
            else:
                self.addRec(atual.esquerda, no, atual)
        else:
            raise Exception("valor ja esta na lista")

    def buscar(self, valor):
        atual = self.__raiz

        if atual.valor == valor:
            return atual
        else:
            no = self.buscarNoRec(atual, valor)
            if no is None:
                raise Exception("valor não esta na arvore")
            else:
                return no

    def buscarNoRec(self, atual, valor):
        if atual is None:
            return atual
        elif atual.valor > valor:
            return self.buscarNoRec(atual.esquerda, valor)
        elif atual.valor < valor:
            return self.buscarNoRec(atual.direita, valor)
        else:
            return atual

a = ArvoreBuscaBinaria()

a.add(1)
a.add(2)
a.add(3)
a.add(4)
a.add(5)

print(a.buscar(3))