"""
Faça um programa que receba três notas e seus respectivos pesos, calcule e mostre a média ponderada.

O usuário deverá digitar os valores para: nota1 e peso1, nota2 e peso2, por fim, nota3 e peso3.

O programa deverá exibir o resultado da média ponderada com duas casas decimais de precisão.

OBS: O programa não deverá colocar enfeites/perfumaria ao esperar o usuário digitar, bem como, ao mostrar o resultado na tela. Observe o exemplo a seguir.

Exemplo:
Dados de entrada:

7.25
3.5
8.87
3.5
1.24
3
Dados de saída:

6.01
"""
nota1 = float(input(""))
peso1 = float(input(""))
nota2 = float(input(""))
peso2 = float(input(""))
nota3 = float(input(""))
peso3 = float(input(""))
print("{:.2f}".format(((nota1 * peso1) + (nota2 * peso2) + (nota3 * peso3)) / (peso1 + peso2 + peso3)))