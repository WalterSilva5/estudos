def ordenador():
    lista = []
    while True:
        palavra = input("Digite:")
        if palavra =='b':
            break
        else:
            lista.append(palavra)
    print(lista)
    salva(lista)    
    
def salva(lista):
    lista.sort()
    
    arquivo = open('arquivo.txt','w')
    for x in lista:
        arquivo.write(x+'\n')
    arquivo.close()
ordenador()
