salarioBruto = float(input(""))
if salarioBruto <= 350:
	salarioBruto+=(-(salarioBruto/100)*7)+100

elif salarioBruto > 350 and salarioBruto <600:
	salarioBruto+=(-(salarioBruto/100)*7)+75


elif salarioBruto >= 600 and salarioBruto <=900:
	salarioBruto+=(-(salarioBruto/100)*7)+50

else:
	salarioBruto+=(-(salarioBruto/100)*7)+35

print("{:.2f}".format(salarioBruto))
