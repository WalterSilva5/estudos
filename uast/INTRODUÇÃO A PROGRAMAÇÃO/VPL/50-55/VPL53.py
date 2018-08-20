#numeros decrescentes
inicio = int(input(""))
fim = int(input(""))

def funcao(inicio, fim):
    if inicio >= fim:
        print(inicio)
        return (funcao(inicio-1, fim))
    
funcao(inicio,fim)
