"""VPL - Atividade 33 (Eleição)

Numa eleição existem três candidatos (candidatos: 1, 2 e 3, branco = 0).
 Faça um programa que receba o número total de eleitores que irão votar.
 Peça para cada eleitor votar e ao final mostrar o número de votos de cada candidato.

A saída dever ser:

"Candidato 1 = #, Candidato 2 = #, Candidato 3 = #, Branco = #, Nulo = #."

*O jogo da velha deve ser substituído pelo número.

**A ordem dos candidatos deve ser impressa de acordo com a quantidade de votos (ordem decrescente)."""
from random import *
branco =0
c1 = 0
c2 = 0
c3 = 0
nulo = 0
eleitores = int(input("Nº de Eleitores: "))

for x in range(eleitores):
    voto = int(input("Voto: "))

    if voto == 0:
        branco+=1

    elif voto == 1:
        c1+=1
    elif voto == 2:
        c2+=1
    elif voto == 3:
        c3+=1
    else:
        nulo+=1

if c1 >= c2 >= c3:
    print("candidato  1 = {}, Candidato 2 = {}, candidato 3 ={}, branco = {} nulo ={}".format(c1,c2,c3,branco,nulo))

elif c3 >= c1 >= c2:
    print("candidato  3 = {}, Candidato 1 = {}, candidato 2 ={}, branco = {} nulo ={}".format(c3,c1,c2,branco,nulo))

elif c2>= c1>= c3:
    print("candidato  2 = {}, Candidato 1 = {}, candidato 3 ={}, branco = {} nulo ={}".format(c2, c1, c3, branco, nulo))
elif c1>= c3>= c2:
    print("candidato  1 = {}, Candidato 3 = {}, candidato 2 ={}, branco = {} nulo ={}".format(c1, c3, c2, branco, nulo))

elif c2>= c3>= c1:
    print("candidato  2 = {}, Candidato 3 = {}, candidato 1 ={}, branco = {} nulo ={}".format(c2, c3, c1, branco, nulo))
