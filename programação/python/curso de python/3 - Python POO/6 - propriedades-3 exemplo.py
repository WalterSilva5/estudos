class Retangulo(object):
    def __init__(self, altura, largura):
        self._largura = 0
        self._altura = 0
        self.largura = altura
        self.largura = largura
    @property
    def altura():
        return self._altura
    @altura.setter
    def altura(self, num):
        if(not(isinstance(num, int) and(num>0))):
            raise ValueError("Altura Invalida".format(num))
        self._altura = num

    @property
    def largura(self):
        return self._largura
    @largura.setter
    def largura(self, num):
        if(not(isinstance(num, int) and(num>0))):
            raise ValueError("largura Invalida".format(num))
        self._largura = num

    #quando temos apenas a @property significa que o atributo é apenas de leitura
    @property
    def area(self):
        return self._altura*self._largura

ex de uso:
r = Retangulo(largura = 5, altura = 10)
r.largura
r.altura

print(r.largura)
print(r.altura)
