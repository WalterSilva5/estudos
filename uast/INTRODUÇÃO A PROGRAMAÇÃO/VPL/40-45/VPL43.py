"""VPL - Atividade 43 (Vetores para Matriz)
Faça um programa que crie dois vetores, usando listas e, receba 6 números
 inteiros em cada um dos vetores. Por fim, o programa deverá criar
 uma matriz 3x4 a partir da intercalação dos dois vetores.


Essa intercalação se dará da seguinte forma:

            Captura dois elementos do vetor1 e coloca na matriz
            Captura dois elementos do vetor2 e coloca na matriz
            Repete até preencher a matriz

Além disso, os elementos capturados serão inseridos um ao lado do
 outro na matriz, caso a linha acabe, deverá inserir na próxima linha e assim sucessivamente.
"""

lista1 = list(range(1,11))
lista2 = list(range(11,21))
matriz =[]

c=0
while True:
    matriz.append([])
    matriz[c].append(lista1[0])
    matriz[c].append(lista2[0])
    lista1.pop(0)
    lista2.pop(0)
    c+=1
    if len(matriz)== 10:
        break

print(matriz)