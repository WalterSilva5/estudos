#coding=utf-8
quant = (int(input("Quantidade de elementos: ")))
lista = []
cont = 0
cont2 = 0
media =0
def funcao(lista, media, cont, cont2):
    cont+=1
    if cont -1 == quant:
        mostrar(media,lista, cont2)
    else:
        elemento = float(input(""))
	media+= elemento
	lista.append(elemento)
        return(funcao(lista,media,cont, cont2))


def mostrar(media, lista, cont2):
    #print(media/len(lista))
    if cont2 < len(lista):
        print("O elemento do índice {} é: {}".format(cont2, lista[cont2]))
        cont2+=1
	return(mostrar(media, lista,cont2))
    else:
	print(media)
        print("Media: {:.2f}".format(media/len(lista)))

funcao(lista, media, cont, cont2)


