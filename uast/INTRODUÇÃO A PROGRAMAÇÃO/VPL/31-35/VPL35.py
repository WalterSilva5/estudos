"""VPL - Atividade 35 (Base e Expoente)
Faça um programa que peça dois números, base e expoente, calcule e mostre
o primeiro número elevado ao segundo número usando apenas estrutura de repetição.

	A saída deve ser:

	"# ^ # = #"

	*O jogo da velha deve ser substituído pelo número.

"""

valor = int(input("Valor: "))
expoente = int(input("Expoente: "))
nvalor = 0
for x in range(expoente-1):
    nvalor += (valor*valor)
    print(valor)

print("{}^{}={}".format(valor, expoente,nvalor))