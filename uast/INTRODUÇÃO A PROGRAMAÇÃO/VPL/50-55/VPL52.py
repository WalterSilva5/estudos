inicial = int(input(""))
final = int(input(""))

def funcao(inicial, final):
    if inicial <=final:
        print(inicial)
        return (funcao(inicial+1, final))
funcao(inicial, final)

