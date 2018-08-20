"""
Faça um programa que receba três notas, calcule e mostre a média aritmética.

O usuário deverá digitar os valores para nota1, nota2 e nota3.

O programa deverá exibir o resultado da média aritmética com duas casas decimais de precisão.

OBS: O programa não deverá colocar enfeites/perfumaria ao esperar o usuário digitar, bem como, ao mostrar o resultado na tela. Observe o exemplo a seguir.

Exemplo:
Dados de entrada:

8.36
4.56
1.44
Dados de saída:

4.79
"""
nota1 = float(input(""))
nota2 = float(input(""))
nota3 = float(input(""))
print("{:.2f}".format((nota1 + nota2 + nota3) / 3))