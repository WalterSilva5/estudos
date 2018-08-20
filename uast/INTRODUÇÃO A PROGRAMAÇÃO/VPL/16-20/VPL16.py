"""
VPL - Atividade 16 (Situação de um Aluno)
Ao receber três notas de um aluno, o algoritmo deverá calcular a média das três notas e
imprimir a situação do aluno de acordo com sua média:
Aprovado se média >= 7
Exame Final se média >= 4 e média < 7
Reprovado se média < 4
"""

n1 = float(input(""))
n2 = float(input(""))
n3 = float(input(""))

media = n1+n2+n3/3

if media >=7:
    print("Aprovado")
elif media >=4 and media<7:
    print("Exame Final")
else:
    print("Reprovado")