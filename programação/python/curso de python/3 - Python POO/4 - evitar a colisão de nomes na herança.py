ao colocar em uma variavel dentro da classe dois underlines
essa variavel externamente para ser ultilizada sera renomeada

então para a ultilizarmos termos que fazer _Classe__variavel

por ex:
classe Numeros(object):
    def__init__(self):
        __n = 10

num = Numeros()

e para usarmos a variavel __n temos que fazer:
_Numeros__n

ex:
print(_Numeros__n)

desse modo evitamos a colisão de nomes ao extender uma classe
