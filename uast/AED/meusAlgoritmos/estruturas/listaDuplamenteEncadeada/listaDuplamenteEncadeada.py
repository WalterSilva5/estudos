class ListaDuplamenteEncadeada(object):
    def __init__(self):
        self.inicio = None
        self.__tam = 0

    class No:  
        def __init__(self, valor):
            self.anterior = None
            self.valor = valor
            self.proximo = None

    def adicionar(self, valor):
        atual = self.inicio
        no = self.No(valor)
        if self.inicio is None:
            self.inicio = no
        else:
            while atual.proximo is not None:
                atual = atual.proximo
            atual.proximo = no
            
    def remover(self, valor):
        atual = self.inicio
        if self.fim.valor == valor:
            self.fim = self.fim.anterior
            self.fim.proximo = self.inicio
        else:
            while atual.valor != valor and atual is not self.fim:
                atual = atual.proximo
                
        
        
    def listar(self):
        lista = "["
        atual = self.inicio
        while atual.proximo is not None:
            lista+="{}, ".format(str(atual.valor))
            atual = atual.proximo
        lista+="]"
        return lista
