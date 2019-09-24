class Lista(object):
    def __init__(self):
        self.inicio = None
        self.fim = None
        self.meio = None
        self.__tam = 0
        self.posicaoMeio = 0
        
    class No:
        def __init__(self, valor):
            self.valor = valor
            self.anterior = None
            self.proximo = None

    def moveMeioParaFrente(self):
        if self.__tam%2 == 0:
            self.meio = self.meio.proximo
            self.posicaoMeio+=1

    def moveMeioParaTras(self):
        if self.__tam%2 == 0:
            self.meio = self.meio.anterior
            self.posicaoMeio-=1

    def adicionar(self, valor):
        no = self.No(valor)
        if self.fim is None:
            self.inicio = no
            self.inicio.anterior = no
            self.inicio.proximo = no
            self.fim = self.inicio
            self.meio = self.inicio
        else:
            no.proximo=self.inicio
            self.fim.proximo = no
            no.anterior = self.fim
            self.fim = no
            self.inicio.anterior = self.fim
            self.moveMeioParaFrente()

        self.__tam +=1

    def __str__(self):
        if self.__tam==0:
            return "[]"

        cont = 0
        texto = "["
        atual = self.inicio
        while cont <self.__tam:
            texto+="{}, ".format(str(atual.valor))
            atual = atual.proximo
            cont+=1

        texto=texto[:-2]+"]"
        return texto

    def buscarPosicao(self, valor):
        atual = self.inicio
        cont = 0

        while atual.valor is not valor and atual is not self.fim:
            cont+=1
            atual = atual.proximo

        if atual == self.fim and atual.valor != valor:
            return "Não está na lista"
        else:
            return cont

    def buscarPorValor(self, valor):
        atual = self.inicio

        while atual.valor is not valor and atual is not self.fim:
            atual = atual.proximo

        if atual == self.fim and atual.valor != valor:
            return None
        else:
            return atual
    
    def buscarPorPosicao(self, posicao):
        if posicao <0 or posicao > self.__tam:
            return "Não esta na lista"
        atual = self.meio
        cont = self.posicaoMeio
        if posicao > self.posicaoMeio:
            while cont < posicao-1:
                atual = atual.proximo
                cont+=1
        else:
            while cont>posicao-1:
                atual = atual.anterior
                cont-=1

        return cont

lista = Lista()
lista.adicionar(1)
lista.adicionar(2)
lista.adicionar(3)
lista.adicionar(4)
lista.adicionar(5)
lista.adicionar(6)
lista.adicionar(7)
lista.adicionar(8)
lista.adicionar(9)


print(lista.posicaoMeio)
print(lista.meio.valor)

print(lista.buscarPorPosicao(5))
