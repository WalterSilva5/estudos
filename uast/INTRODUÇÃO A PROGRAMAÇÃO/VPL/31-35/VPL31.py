"""PL - Atividade 31 (Pares e Ímpares)
Faça um programa que peça 10 números inteiros, calcule e mostre a
quantidade de números pares e a quantidade de números impares.

A saida dever ser:
	"Pares = #, Ímpares = #."
	*O jogo da velha deve ser substituído pelo número.
	"""
import random

lista100 = list(range(1,100))

random.shuffle(lista100)
lista = lista100[0:10]
pares = 0
impares = 0

for x in lista:
    if x %2 == 0:
        pares += 1
    else:
        impares += 1

print("Pares: {}, Impares: {}".format(pares, impares))