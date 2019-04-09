#coding=utf-8
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
            print("adiciona no inicio")
        elif indice == self.__tamanho:
            no = No(elemento)
            perc = self.inicio
            self.inicio = no
            no.proximo = perc
            self.__tamanho +=1
        else:
            no = No(elemento)


    def getIndex(self, indice):
        perc = self.inicio
        if self.__tamanho==0:
            return "[]"
        count = 0
        while perc.proximo != None
            if count == indice:
                break
            perc = perc.proximo
            cont+=1
        return perc.elemento






    def append(self):
        pass

    def __len__(self):
        return self.__tamanho
    def __str__(self):
        result = "[{}, ".format(self.inicio.elemento)
        perc = self.inicio
        while perc.proximo is not None:
            perc=perc.proximo
            result+="{}, ".format(perc.elemento)

        result = result[:-2]
        result+="]"
        return result

ll = Lista()

ll.add("a")
ll.add("b")
ll.add("c")
ll.add("d")
print(ll)
ll.pop()
