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

    def inserir(self, posicao, valor):
        no = self.No(valor)
        if posicao == self.__tam:
            self.adicionar(valor)
        else:
            antigo = self.buscarPorPosicao(posicao)
            no.proximo = antigo
            no.anterior = antigo.anterior
            antigo.anterior.proximo = no
            self.__tam +=1
            self.moveMeioParaFrente()

    def removerPorValor(self, valor):
        vaiRemover = self.buscarPorValor(valor)
        vaiRemover.anterior.proximo = vaiRemover.proximo
        self.__tam-=1
        self.moveMeioParaTras()

    def removerPorIndice(self, posicao):
        vaiRemover = self.buscarPorPosicao(posicao)
        vaiRemover.anterior.proximo = vaiRemover.proximo
        self.__tam-=1
        self.moveMeioParaTras()


    def editar(self, posicao, valor):
        no = self.buscarPorPosicao(posicao)
        no.valor = valor

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

    def listarComIndices(self):
        if self.__tam==0:
            return "[]"

        cont = 0
        texto = "["
        atual = self.inicio
        while cont <self.__tam:
            texto+="'P{}': {}, ".format(cont,str(atual.valor))
            atual = atual.proximo
            cont+=1

        texto=texto[:-2]+"]"
        return texto

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
            raise IndexError("Index fora da lista")
        atual = self.meio
        cont = self.posicaoMeio
        if posicao > self.posicaoMeio:
            while cont < posicao:
                atual = atual.proximo
                cont+=1
        else:
            while cont>posicao:
                atual = atual.anterior
                cont-=1

        return atual

