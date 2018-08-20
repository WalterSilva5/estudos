"""PL - Atividade 24 (Faixa etária)
Disponível até: segunda, 30 Out 2017, 08:00
Número máximo de arquivos: 1
Tipo de trabalho: Trabalho individual
Faça um programa que receba a idade de oito pessoas, calcule e mostre:
            a quantidade de pessoas em cada faixa etária;
            a porcentagem de pessoas na primeira faixa etária com relação ao total de pessoas.
            a porcentagem de pessoas na última faixa etária com relação ao total de pessoas
FAIXA ETÁRIA
IDADE
1ª
Até 15 anos
2ª
De 16 a 30 anos
3ª
De 31 a 45 anos
4ª
De 46 a 60 anos
5ª
Acima de 60 anos
OBS:
    Você precisará fazer uso de estruturas de decisão (por exemplo: if, elif ou else)
    Você precisará fazer uso de estruturas de repetição (por exemplo: while)
    Respeite a formatação para exibir os dados na tela. Observe o exemplo a seguir."""

faixa1=0
faixa2=0
faixa3=0
faixa4=0
faixa5=0

for x in range(8):
    pessoa = float(input("Digite a idade da {} pessoa: ".format(x)))
    if pessoa <= 15:
        faixa1+=1
    elif pessoa >=16 and pessoa <=30:
        faixa2+=1
    elif pessoa>=31 and pessoa <=45:
        faixa3+=1
    elif pessoa >=46 and pessoa <=60:
        faixa4+=1
    else:
        faixa5+=1

total = faixa1+faixa2+faixa3+faixa4+faixa5
print (total)
pct = (total/100)*faixa1
print(pct)
print(faixa1)
print(faixa2)
print(faixa3)
print(faixa4)
print(faixa5)
