"""VPL - Atividade 15 (Operações matemáticas com Idades)

Escreva um algoritmo que leia as idades de 2 homens e de 2 mulheres (considere que todos possuem
 idades distintas entre si). Calcule a soma das idades do homem mais velho com a mulher mais nova
  (“salve esse resultado em uma variável X”), depois calcule o produto das idades do homem mais
  novo com a mulher mais velha (“salve esse resultado em uma variável Y”).

De posse de X e Y realize a subtração do maior pelo menor e imprima o resultado dessa subtração .


OBS:

    Você precisará fazer uso de estruturas condicionais (por exemplo: if, elif ou else)
    O programa deverá exibir o resultado sem casas decimais ("idades são valores inteiros")
    O programa não deverá colocar enfeites/perfumaria ao esperar o usuário digitar, bem
    como, ao mostrar o resultado na tela. Observe o exemplo a seguir.
    """

x = int(input("HOMEM MAIS VELHO"))
x+= int(input("MULHER MAIS NOVA"))
y = int(input("HOMEM MAIS NOVO"))
y*= int(input("MULHER MAIS VELHA"))

if x > y:
    x-=y
    print(x)
else:
    y-=x
    print(y)