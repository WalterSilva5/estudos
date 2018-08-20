"""VPL - Atividade 19 (Ímpar ou Par ?)
Disponível até: segunda, 30 Out 2017, 08:00
Número máximo de arquivos: 1
Tipo de trabalho: Trabalho individual
Faça um programa que receba do usuário, um número inteiro e diga se ele é: Par ou Ímpar.

OBS:

    Você precisará fazer uso de estruturas condicionais (por exemplo: if, elif ou else)
    Respeite a formatação para exibir os dados na tela. Observe o exemplo a seguir."""

n = int(input(": "))

if n %2 ==0:
    print("Par")
else:
    print("impar")