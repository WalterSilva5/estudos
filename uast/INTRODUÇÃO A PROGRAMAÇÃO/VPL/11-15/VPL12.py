tipo = int(input(""))
valor = float(input(""))
if tipo ==1:
	valor+=(valor/100)*3
elif tipo ==2:
	valor+=(valor/100)*4
print("{:.2f}".format(valor))

input("")