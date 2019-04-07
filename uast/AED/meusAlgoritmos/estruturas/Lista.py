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

    def __len__(self):
        return self.tamanho
    def __str__(self):
        result = "["
        perc = self.inicio
        while perc.proximo is not None:
            perc = perc.proximo
            result+=", {}".format(.elemento)
        result+="]"
        return result

ll = Lista()
ll.add("a")
ll.add("b")
ll.add("c")
ll.add("d")

print(ll)
