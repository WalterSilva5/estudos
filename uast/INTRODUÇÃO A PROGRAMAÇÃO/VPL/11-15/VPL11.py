produto = float(input(""))
if produto<=50: 
	produto+=(produto/100)*5
elif produto>50 and produto<=100:
	produto+=(produto/100)*10
else:
	produto+=(produto/100)*15

if produto<=80: 
	print("{:.2f} barato".format(produto))
elif produto>80 and produto<=120:
	print("{:.2f} normal".format(produto))
elif produto>120 and produto<=200:
	print("{:.2f} caro".format(produto))
else:
	print("{:.2f} muito caro".format(produto))
