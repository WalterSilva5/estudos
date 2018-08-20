"""VPL - Atividade 41 (Quantidade de elementos na matriz)
Faça um programa que preencha uma matriz 3 x 5 (3 linhas e 5 colunas) com números inteiros.
Posteriormente, mostre a matriz montada, calcule e mostre a quantidade de elementos entre 15 e 20.
Dica: ao montar a matriz formatada no console, o espaçamento entre um elemento e outro deve ser com \t."""
import random
lista100 = list(range(1,99))
random.shuffle(lista100)
matriz = []
valores = 0
for x in range(3):
    matriz.append([])
    for y in range(5):
        matriz[x].append(lista100[0])
        lista100.pop(0)
for x in range(3):
    for y in range(5):
        print(matriz[x][y],end="\t")
    print(end="\n")

for x in range(3):
    for y in range(5):
        if matriz[x][y]>=15 and matriz[x][y] <=20:
            valores+=1
print("Quantidade de elementos entre 15 e 20: {}".format(valores))
