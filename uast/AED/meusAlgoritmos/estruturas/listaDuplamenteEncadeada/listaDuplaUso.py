from listaDuplamenteEncadeada import ListaDuplamenteEncadeada
from listaSimples import ListaDuplamenteEncadeada as listaSimples

import time

listaDuplaA = ListaDuplamenteEncadeada()
listaDuplaB = listaSimples()

inicioA = time.time()

for n in range(10000):
    listaDuplaA.adicionar(n)
    
fimA = time.time()

print("Tempo de execução: {:.2f} seg".format(fimA - inicioA))

inicio = time.time()

for n in range(10000):
    listaDuplaB.adicionar(n)
fim = time.time()

print("Tempo de execução: {:.2f} seg".format(fim - inicio))
