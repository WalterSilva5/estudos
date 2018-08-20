saldoMedio = float(input(""))
if saldoMedio <= 200:
    percentual = (saldoMedio / 100) * 10
elif saldoMedio > 200 and saldoMedio <= 300:
    percentual = (saldoMedio / 100) * 20
elif saldoMedio > 300 and saldoMedio <= 400:
    percentual = (saldoMedio / 100) * 25
else:
    percentual = (saldoMedio / 100) * 30
print("{:.2f}  {:.2f}".format(saldoMedio, percentual))