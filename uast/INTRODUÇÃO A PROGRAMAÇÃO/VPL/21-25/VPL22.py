"""VPL - Atividade 22 (Semana)
Disponível até: segunda, 30 Out 2017, 08:00
Número máximo de arquivos: 1
Tipo de trabalho: Trabalho individual
Faça um programa que leia um número e exiba o dia correspondente da semana.
Por exemplo: (1 - Domingo, 2 - Segunda, 3 - Terça, ... ... , 7 - Sábado),
 se digitar um valor não correspondente, o programa deverá exibir: Inválido.
OBS:
    Você precisará fazer uso de estruturas condicionais (if, elif, else)
    O programa não deverá colocar enfeites/perfumaria ao esperar o usuário digitar,
    bem como, ao mostrar o resultado na tela. Observe o exemplo a seguir."""

dia = int(input("DIa: "))

if dia == 1:
    print("Domingo")
elif dia == 2:
    print("Segunda")
elif dia == 3:
    print("Terça")
elif dia == 4:
    print("Quarta")
elif dia == 5:
    print("Quinta")
elif dia == 6:
    print("Sexta")
elif dia == 7:
    print("Sabado")
elif dia == 8:
    print("Domingo")
else:
    print("Dia invalido")
