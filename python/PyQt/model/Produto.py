class Produto(object):
    def __init__(self, nome, codigo, valor):
        self.__nome = ""
        self.__codigo = 0
        self.__valor = 0.0

        self.nome = nome
        self.codigo = codigo
        self.valor = valor
    
    @property
    def nome(self):
        return self.__nome
    @nome.setter
    def nome(self, nome):
        self.__nome = nome

    @property
    def codigo(self):
        return self.__codigo
    @codigo.setter
    def codigo(self, codigo):
        self.__codigo = codigo

    @property
    def valor(self):
        return self.__valor
    @valor.setter
    def valor(self, valor):
        self.__valor = valor


