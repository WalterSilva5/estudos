"""VPL - Atividade 38 (Fatorial de Primo ou Somatório do Duplo Fatorial)
Disponível até: segunda, 6 Nov 2017, 08:00
Número máximo de arquivos: 1
Tipo de trabalho: Trabalho individual
Crie um programa que receba do usuário um número inteiro e positivo X,
caso ele seja um número primo, imprima o fatorial desse número,
do contrário realize o somatório do duplo fatorial
de todos os elementos pares contidos no intervalo de 1 a X.
"""

n = int(input("N: "))
aux = n
divisores = 0
for x in range(1,n+1):
    if n%x==0:
        divisores+=1

if divisores ==2:
    temp = n
    for x in range(n-1):
        n *= temp-1
        temp-=1
    print("O fatorial de {} é {}".format(aux,n))
else:
    temp = aux
    for x in range(aux//2-1):
        temp -= 2
        aux *= temp
    print("Os somatorios dos duplos fatoriais de {} é {}".format(n,aux))
