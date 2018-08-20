"""VPL - Atividade 34 (Tabuada)

Faça um programa que gera a tabuada de multiplicação de qualquer número inteiro.
O usuário deve informar de qual número ele deseja ver a tabuada
e até onde deve ser calculado a tabuada (de um a N).

	A saída deve ser:

	"# x # = #"

	*O jogo da velha deve ser substituído pelo número.

"""
valor = int(input("Valor: "))
limite = int(input("Limite: "))

for x in range(1,limite):
    print(("{}x{}={}".format(valor,x,valor*x)))