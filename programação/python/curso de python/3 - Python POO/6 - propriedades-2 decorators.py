#https://pythonacademy.com.br/blog/domine-decorators-em-python
O  conceito de decorator provê uma maneira simples de modificar
o comportamento de uma função sem necessariamente alterá-la.

#explicação:
para usar os decorators em um atributo
nos definimos o atributo como privado: _x
e então criamos metodos com o nome do atributo
porem esses metodos são publicos

então para começar
o atributo x por exemplo
para o getter o decorator é apenas o @property

para o setter do decorator apenas criamos uma função que recebe um parametro
e sua propriedade sera @x.setter

ex:

class A:
    def __init__(self):
        self._x = 0

    @property
    def x(self):
        return self._x
    @x.setter
    def x(self, val):
        self._x = val
    #@x é o nome do decorator
    #setter é a açõa que esse metodo executa


ex de uso:
a = A()

não precisamos usar parenteses para usar os metodos de decorators
então para acessar o valor da variavel x usando decorator basta fazer:
######
a.var = 10
atribuimos um valor a variavel x sem precisar passar um parametro para o setter

#####
t = a.var
e isso ja retorna pra variavel t o valor que o metodo getter do x retorna
