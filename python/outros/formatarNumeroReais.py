lista = [1,2,3,4,5,6,7,8,9,10]

cont=0
matriz=[]

while cont <len(lista):
    for x in range(3):
        try:
            matriz.append(lista[cont])
            cont+=1
        except:
            break
    matriz.append(",")
    
teste = ","
if matriz[-1] is teste:
    matriz.pop()

matriz.reverse()
nNum = ""
for elemento in matriz:
    nNum+=str(elemento)
print(nNum)