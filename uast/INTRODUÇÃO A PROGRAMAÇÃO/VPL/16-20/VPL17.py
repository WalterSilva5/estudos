"""VPL - Atividade 17 (Maior, igual ou menor do que Y)

Faça um algoritmo que receba dois  números X, Y e diga se X é maior, menor ou igual a Y.
"""

x = int(input("X: "))
y = int(input("Y: "))

if x > y:
    print("Maior")
elif x<y:
    print("Menor")
else:
    print("Igual")