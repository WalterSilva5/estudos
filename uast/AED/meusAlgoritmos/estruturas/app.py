arq = open("arvore.py", "r")
arq2 = arq.readlines()
arq3 = ""

for linha in arq2:
    if list(linha)[0] != "#":
        arq3+=linha+"\n"

print(arq3)