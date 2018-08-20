#exemplo de codigo usando getter e setter pra nao dar erro

class Retangulo(object):
    def __init__(self, largura, altura):
        #criamos os atributos com valores default
        self.largura = 0
        self.altura = 0
        #invocamos os setters no construtor
        self.set_altura(altura)
        self.set_largura(largura)

    def set_altura(self, num):
        #usamos o setter pra verificar antes de atribuir
        if(not(isinstance(num, int) and (num > 0))):
            raise ValueError("Altura é invalida: {}".format(num))
        self.altura = num

    def set_largura(self, num):
        #usamos o setter pra verificar antes de atribuir
        if(not(isinstance(num, int) and (num > 0))):
            raise ValueError("Largura é invalida: {}".format(num))
        self.largura = num

    def get_area(self):
        #retornamos os valores verificados
        return self.largura * self.altura


r = Retangulo(altura = 10, largura = 5)

print(r.get_area())
