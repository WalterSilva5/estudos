"""VPL - Atividade 32 (Quanto é H para N)
Sendo H= 1 + 1/2 + 1/3 + 1/4 + ... + 1/N, Faça um programa que
 calcule o valor de H com N termos. O programa deverá receber
 a variável N para poder calcular H.

	A saida dever ser:

		"H = #"

		*O jogo da velha deve ser substituído pelo número.

"""

h = 1

n = int(input("N: "))
cont = 2
for x in range(n+1):
    h += 1/cont
    cont+=1

print("{:.2f}".format(h))
