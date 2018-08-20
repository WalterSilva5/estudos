"""Faça um programa que recebe uma letra e diga se a letra digitada é
uma vogal ou consoante. Considere que serão digitadas apenas letras.

Imprima apenas Vogal para vogal e Consoante para consoante."""

vogais = "aeiou"
letra = input("Letra: ").lower()

tipo = ""
for l in vogais:
    if letra == l:
        tipo = "vogal"
        break
    else:
        tipo = "consoante"
print (tipo)