salarioAtual = float(input(""))
if salarioAtual <= 300:
    almento = (salarioAtual / 100) * 15
elif salarioAtual > 300 and salarioAtual < 600:
    almento = (salarioAtual / 100) * 10
elif salarioAtual >= 600 and salarioAtual <= 900:
    almento = (salarioAtual / 100) * 5
else:
    almento = 0
print("{:.2f}  {:.2f}".format(almento, salarioAtual + almento))