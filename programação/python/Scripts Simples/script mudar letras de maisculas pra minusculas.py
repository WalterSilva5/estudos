def programa():
	print ("Escolha uma opção:")
	print ("Para Maiusculas MA")
	print ("Para Minusculas MI")
	print ("Para Titulo TI")
	op = input("Digite a opção desejada: ").lower()

	if op == "ma":
		Maiusculas()
	elif op == "mi":
		Minusculas()
	elif op =="ti":
		Titulo()

def Maiusculas():
	arquivo = open('arquivo.txt','r')
	texto = arquivo.read()
	arquivo.close()
	
	texto = texto.upper()
	arquivo = open('arquivo.txt','w')
	arquivo.write(texto)
	arquivo.close()

	print("Letras No arquivo.txt Ficaram Maisculas.")
	exit()

def Minusculas():
	arquivo = open('arquivo.txt','r')
	texto = arquivo.read()
	arquivo.close()
	
	texto = texto.lower()
	arquivo = open('arquivo.txt','w')
	arquivo.write(texto)
	arquivo.close()

	print("Letras No arquivo.txt Ficaram Minusculas.")
	exit()
	
def Titulo():
	arquivo = open('arquivo.txt','r')
	texto = arquivo.read()
	arquivo.close()
	
	texto = texto.upper()
	arquivo = open('arquivo.txt','w')
	arquivo.write(texto)
	arquivo.close()

	print("Letras No arquivo.txt Ficaram Maisculas.")
	exit()


programa()
