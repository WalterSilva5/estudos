"""VPL - Atividade 25 (Primo)
Faça um programa que receba um número inteiro e mostre se é ou não primo, além disso, mostre também quantos divisores esse número possui.

OBS:

Você precisará fazer uso de estruturas de decisão (por exemplo: if, elif ou else)
Você precisará fazer uso de estruturas de repetição (por exemplo: while)"""

n = int(input("n: "))
divis=[]
cont = 1

while cont <=n:
    if n % cont==0:
        divis.append(cont)
    cont+=1

if len(divis)==2:
    print("{} é primo e possui {} divisores.".format(n, len(divis)))
else:
    print("{} não é primo e possui {} divisores.".format(n, len(divis)))