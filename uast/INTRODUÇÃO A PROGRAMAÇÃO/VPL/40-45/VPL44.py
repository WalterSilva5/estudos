"""VPL - Atividade 44 (Manipulação com Matrizes)
Faça um programa que preencha com números inteiros, uma matriz M 3x4. Deve-se identificar qual é o maior elemento dessa matriz M.

Posteriormente, uma matriz R, também 3x4, deverá ser formada a partir da divisão dos elementos de M pelo maior elemento de M.

Por fim, o programa deverá criar a matriz F 3x4, onde cada elemento de F deverá ser:

            A soma da multiplicação do maior elemento da matriz M pelo respectivo elemento de R, com a divisão do respectivo elemento de M pela média de todos os elementos da matriz R.
            Ex: (maior_m * r[i][j]) + (m[i][j] / média_r)

Todas as três matrizes geradas devem ser impressas de acordo com a formatação do exemplo ilustrado a seguir. Todos os números floats devem ser impressos com apenas uma casa decimal de precisão.

"""
import random
lista = list(range(1,100))
random.shuffle(lista)
matrizM = []
matrizR = []
c = 0
maior = 0

for x in range(3):
    matrizM.append([])
    for j in range(4):
        matrizM[x].append(lista[c])
        if lista[c]>maior:
            maior = lista[c]
        c+=1
print(matrizM)

for x in range(3):
    matrizR.append([])
    for j in range(4):
        matrizR[x].append(matrizM[x][j]/maior)

print(matrizR)