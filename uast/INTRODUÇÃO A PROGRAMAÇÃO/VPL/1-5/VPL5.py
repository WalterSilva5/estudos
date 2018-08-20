custoDeFabrica = float(input(""))
if custoDeFabrica <= 12000:
    custoDeFabrica += (custoDeFabrica / 100) * 5
elif custoDeFabrica > 12000 and custoDeFabrica <= 25000:
    custoDeFabrica += (custoDeFabrica / 100) * 25
else:
    custoDeFabrica += (custoDeFabrica / 100) * 35
print("{:.2f}".format(custoDeFabrica))