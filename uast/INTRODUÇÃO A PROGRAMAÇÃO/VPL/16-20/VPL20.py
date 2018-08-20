"""VPL - Atividade 20 (Data válida)
Disponível até: segunda, 30 Out 2017, 08:00
Número máximo de arquivos: 1
Tipo de trabalho: Trabalho individual

Escreva um programa que leia o dia, mês e ano do aniversário de uma pessoa e
diga se a data é válida ou não (Retorna True para válido e False se não for válido).
Suponha que todos os meses tem 31 dias e que a maior data possível seja 21/10/2017."""

#n de dias de 00/00/0000 ate 21/10/217
diasMaiorPossivel = 728468
dias = 0
dia = int(input("Dia: "))
mes = int(input("Mes: "))
ano = int(input("Ano: "))
temp = True
if dia <0 or dia>31:
    temp = False
elif mes <0 or mes> 12:
    temp = False
elif ano < 0 or ano > 2017:
    temp = False
else:
    dias += dia+(mes*31)+(ano*361)
    print(temp)
    if dias > diasMaiorPossivel:
        print("Data Informada Superior a 21/10/2017")

