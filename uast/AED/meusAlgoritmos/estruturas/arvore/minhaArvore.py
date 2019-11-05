class No():
    def __init__(self, valor):
        self.valor = valor
        self.direita = None
        self.esquerda = None

    def __str__(self):
        return str(self.valor)


class Arvore(object):
    def __init__(self):
        self.raiz = None
        self.quantidadeDeFolhas = 0

    def add(self, valor):
        no = No(valor)
        if self.raiz is None:
            self.raiz = no
        else:
            self.addNo(no, self.raiz)
        self.quantidadeDeFolhas += 1
        
    def addNo(self, no, posAtual):
        if no.valor > posAtual.valor:
            if posAtual.direita is None:
                posAtual.direita = no
            else:
                self.addNo(no, posAtual.direita)
        elif no.valor < posAtual.valor:
            if posAtual.esquerda is None:
                posAtual.esquerda = no
            else:
                self.addNo(no, posAtual.esquerda)
        else:
            raise Exception("valor ja esta na arvore")



a = Arvore()
a.add(10)
a.add(5)
a.add(15)
a.add(3)
a.add(3)
