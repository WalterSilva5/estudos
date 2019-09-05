class ListaDuplamenteEncadeada(object):
    def __init__(self):
        self.inicio = None
        self.__tam = 0
        self.fim = None
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
            atual = self.fim
        self.fim = no
        self.__tam +=1
        
    def listar(self):
        lista = "["
        atual = self.inicio
        while atual is not None:
            lista+="{}, ".format(str(atual.valor))
            atual = atual.proximo
        lista=lista[:-2]+"]"
            
        return lista


