from listaDuplamenteEncadeada import Lista

lista = Lista()
lista.adicionar(1)
lista.adicionar(2)
lista.adicionar(3)
lista.adicionar(4)
lista.adicionar(5)
lista.adicionar(6)
lista.adicionar(7)


print(lista.listarComIndices())
print(lista.posicaoMeio)
lista.removerPorIndice(5)
print(lista.listarComIndices())
print(lista.posicaoMeio)