class ListaDupla(object):
    def __init__(self):
        self.inicio = None
        self.__tamanho = 0
    class No:
        def __init__(self, elemento):
            self.elemento = elemento
            self.proximo = None
            self.anterior = None

    def add(self, elemento):
        if self.inicio == None:
            self.inicio = self.No(elemento)
        else:
            no = self.No(elemento)
            perc = self.inicio
            perc.anterior = no
            while perc.proximo != None:
                perc=perc.proximo

            perc.proximo=no
            perc.proximo.anterior = perc
            self.__tamanho +=1

    def __str__(self):
        result = "[{}, ".format(self.inicio.elemento)
        perc = self.inicio
        try:
        while perc.proximo is not None:
            perc=perc.proximo
            result+="anterior:{} /atual:{} / proximo: {} \n".format(perc.anterior.elemento, perc.elemento, perc.proximo.elemento)

        result = result[:-2]
        result+="]"
        except:
            pass
        return result

lista = ListaDupla()
lista.add("a")
lista.add("b")
lista.add("c")
print(lista)
