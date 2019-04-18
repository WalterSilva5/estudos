class Lista(object):
    def __init__(self):
        self.__tamanho = 0
        self.inicio = None

    class No:
        def __init__(self, elemento):
            self.elemento = elemento
            self.proximo = None

    def add(self, elemento):
        no = self.No(elemento)
        if self.inicio is None:
            self.inicio = no
        else:
            perc = self.inicio
            while perc.proximo is not None:
                perc = perc.proximo
            perc.proximo = no
        self.__tamanho +=1

    def addIndex(self, indice, elemento):
        if indice == 0:
            no = self.No(elemento)
            no.proximo = self.inicio
            self.inicio = no
            self.__tamanho += 1
        elif indice == self.__tamanho:
            self.add(elemento)
        else:
            no = self.No(elemento)
            cont = 0
            perc = self.inicio
            while cont < indice-1:
                perc = perc.proximo
                cont+=1
            temp = perc.proximo
            perc.proximo = no
            perc = self.inicio

            while perc.proximo is not None:
                perc = perc.proximo
            perc.proximo = temp

    def __setitem__(self, indice, elemento):
        cont = 0
        perc = self.inicio
        while cont < indice:
            perc = perc.proximo
            cont+=1
        perc.elemento = elemento



    def __str__(self):
        result = "[{}, ".format(self.inicio.elemento)
        perc = self.inicio
        while perc.proximo is not None:
            perc=perc.proximo
            result+="{}, ".format(perc.elemento)

        result = result[:-2]
        result+="]"
        return result

li = Lista()
li.add("a")
li.add("b")
li.add("c")
li.add("d")

li[1] = "K"
print(li)
