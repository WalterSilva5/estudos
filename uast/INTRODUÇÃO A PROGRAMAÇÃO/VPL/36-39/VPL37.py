"""VPL - Atividade 37 (Sequência de Fibonacci)
Disponível até: segunda, 6 Nov 2017, 08:00
Número máximo de arquivos: 1
Tipo de trabalho: Trabalho individual
A sequência de Fibonacci é uma sucessão de números que, misteriosamente,
aparece em muitos fenômenos da natureza. Descrita no final do século 12 pelo italiano
Leonardo Fibonacci, ela é infinita e começa com 0 e 1, os termos restantes são calculados a
 partir da soma dos dois números anteriores a ele.
"""
anterior = 0
proximo = 1
n = int(input("N:"))
for x in range(n):
    aux = proximo
    proximo = anterior + proximo
    anterior = aux
    print(proximo,"",end="")