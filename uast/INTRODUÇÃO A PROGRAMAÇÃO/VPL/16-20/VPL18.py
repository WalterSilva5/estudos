"""VPL - Atividade 18 (Soma do maior com o menor)
Faça um programa que receba 4 números inteiros (considere que todos são distintos entre si)
e retorne a soma do maior número com o menor.

OBS:

    Você precisará fazer uso de estruturas condicionais (por exemplo: if, elif ou else)
    O programa não deverá colocar enfeites/perfumaria ao esperar o usuário digitar, bem como, ao mostrar o resultado na tela.
    """
n1 = int(input("n1: "))
n2 = int(input("n2: "))
n3 = int(input("n3: "))
n4 = int(input("n4: "))

maior = n1
menor = n1


if n2 >= maior:
    maior = n2
if n3 >= maior:
    maior = n3
if n4>= maior:
    maior = n4
if n2 <= menor:
    menor = n2
if n3 <= menor:
    menor = n3
if n4 <= menor:
    menor = n4

print (maior)
print(menor)
print(maior+menor)
