"""VPL - Atividade 23 (Previsão dos lucros)
Disponível até: segunda, 30 Out 2017, 08:00
Número máximo de arquivos: 1
Tipo de trabalho: Trabalho individual

Uma companhia de teatro deseja montar uma série de espetáculos.
Hoje a direção calcula que, se o ingresso custar R$ 5,00, serão vendidos 120 ingressos, e
 que as despesas serão de R$ 200,00. Entretanto, esses valores podem mudar.

Faça um programa para ajudar a direção nessa previsão dos lucros. O programa deverá
 receber o valor do ingresso, a previsão da quantidade de ingressos a serem vendidos e as despesas.

Como saída, o programa deverá exibir uma tabela de valores de lucros esperados em
função do preço do ingresso, fazendo-se esse preço variar do valor informado até R$ 1,00
(ou o valor mais próximo possível), de R$ 0,50 em R$ 0,50.

A cada R$ 0,50 a menos no preço dos ingressos, espera-se que as vendas aumentem em 26 ingressos.

Escreva, para cada novo preço de ingresso, o lucro máximo esperado, o preço do ingresso e
 a quantidade de ingressos vendidos para a obtenção desse lucro."""

valorIngreço = float(input("Valor: "))
quantidadeVendidos = float(input("Quantidade: "))
despesas = float(input("Despesas: "))
lucro = quantidadeVendidos*valorIngreço-despesas
while valorIngreço > 0.50:
    print("{:.2f} / {:.2f} / {:.2f} / {:.2f}".format(valorIngreço, quantidadeVendidos, despesas, lucro))
    valorIngreço-=0.50
    quantidadeVendidos+=26
    lucro = quantidadeVendidos * valorIngreço-despesas
    if valorIngreço<1:
        break