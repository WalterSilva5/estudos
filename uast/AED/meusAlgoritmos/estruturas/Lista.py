class Lista(object):
    def __init__(self):
        self.tamanho = 0
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
        self.tamanho +=1

    def pop(self, indice=None):
        """ao não passar um indice para o metodo pop ele ira remover o ultimo
            elemento da lista e em seguida removelo"""
        print("lista antiga:\n")
        print(self.__str__())
        perc = self.inicio
        ultimo = self.inicio
        if indice == None:
            while perc.proximo is not None:
                perc = perc.proximo
                ultimo = perc.elemento
            perc.elemento=None
        else:
           """ao passar um parametro o metodo pop ira remover o elemento no
               indice definido"""
           while perc.indice is not None:
                if(perc.indice == indice):
                    ultimo = perc.indice
                    perc = None
                    break
                perc = perc.proximo
        print("elemento removido: {}\n".format(ultimo))
        print("nova lista:\n")
        print(self.__str__())
    def append(self):
        pass

    def __len__(self):
        return self.tamanho
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
ll.pop()
