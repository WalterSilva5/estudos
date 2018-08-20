salario = float(input(""))
if salario <=600:
    desconto = 0
elif salario >600 and salario<=1200:
    desconto = (salario/100)*20
elif salario >1200 and salario <=2000:
    desconto = (salario/100)*25
else:
    desconto = (salario/100)*30
print("{:.2f}".format(salario-desconto))