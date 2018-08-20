Em algumas situações, ao criamos uma classe, não desejamos que os
atributos que compõem um objeto dessa classe sejam alterados sem prévia
validação. Para isso, costumamos definir os atributos como privados e
então escrever métodos get_NOME_ATRIBUTO() e set_NOME_ATRIBUTO(),
onde são colocados os testes antes de modificar o objeto.
Podemos usar properties em Python para tornar nosso código
independente de montes de métodos get e set.

#importante
o uso das propriedades possibilita que ao acessarmos um membro diretamente
para atribuir um valor a ele como por exemlo

classe.membro = 'teste'

possamos validar esse valor antes dele ser atribuido

para fazer uma propriedade nos usamos a função property()

ela recebe quatro parametros:
property(fget, fset, fdel, doc)
######################
ex propriedades get e set:
class A:
    def __init__(self):
        self._var = 0
    def get_var(self):
        return self._var
    def set_var (self, value):
        self._var = value
    var = property(fget=get_var, fset=set_var):

a = A()
a.var = 10
print(a.var)
