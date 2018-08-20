"""VPL - Atividade 36 (Maior ou igual, Média)

Faça um programa que recebe a idade e o peso de 10 pessoas e mostre:

Quantidade de pessoas com 90kg ou mais;
Média de idade das pessoas com 90kg ou mais;
Média de peso das pessoas com 90kg ou mais;
Média de peso de todas as pessoas;
Média de idade de todas as pessoas.


	A saída deve ser:

Quantidade de pessoas com 90kg ou mais = #
Média de idade das pessoas com 90kg ou mais = #
Média de peso das pessoas com 90kg ou mais = #
Média de peso de todas as pessoas = #
Média de idade de todas as pessoas = #

	*O jogo da velha deve ser substituído pelos dados.

OBS:"""
import random
pessoas = []
maiorQue90 =[]
for x in range(10):
    idade = random.randrange(10,20)
    peso = random.randrange(40,100)
    pessoas.append([idade,peso])


print(pessoas[1][1])
for x in range(len(pessoas)):
    if pessoas[x][1]>90:
        maiorQue90.append(x)
print(maiorQue90)