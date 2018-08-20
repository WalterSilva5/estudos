class Retangulo:
    def __init__(self, altura, largura):
        self.altura=0
        self.largura=0
        self.set_altura(altura)
        self.set_largura(largura)


    def set_altura(self, num):
        if (not(isinstance(num, int) and (num>0))):
            raise ValueError("Altura Invalida")
        self.altura=num

    def set_largura(self, num):
        if (not(isinstance(num, int) and(num>0))):
            raise ValueError("Largura Invalida")
        self.largura=num

    def get_area(self):
        return self.largura*self.largura


r = Retangulo('a0',10)
print(r.get_area())
