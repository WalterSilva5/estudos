#falta finalizar
linhas = 2
colunas = 2
matriz=[]
linha_atual = 0

def cria_linha(linhas,colunas,matriz,linha_atual):
    if len(matriz) == linhas:
        print(matriz)
    else:
        matriz.append([])
        preenche_coluna(linhas,colunas,matriz,linha_atual)

def preenche_coluna(linhas,colunas,matriz,linha_atual):
    if len(matriz[linha_atual])==colunas:
        cria_linha(linhas,colunas,matriz,linha_atual+1)
    else:
        matriz[linha_atual].append(int(input("N: ")))
        preenche_coluna(linhas, colunas, matriz, linha_atual)
cria_linha(linhas,colunas,matriz,linha_atual)

maior = matriz[0][0]
linha_maior = matriz[0]
n_linha_maior = 0
linha_atual=0
elemento_atual = 0



def verifica_colunas(maior, matriz, elemento_atual):
    if elemento_atual == len(matriz[0]):
        verifica_linhas(maior,matriz,linha_atual+1,elemento_atual=0)

    elif matriz[linha_atual][elemento_atual]>=maior:
        maior = matriz[linha_atual][elemento_atual]
        verifica_colunas(maior, matriz, elemento_atual+1)

def verifica_linhas(maior,matriz,elemento_atual):
    if linha_atual == len(matriz[0]):
        print("maior",maior)
    else:
        verifica_colunas(maior,matriz,elemento_atual)

verifica_linhas(maior,matriz,elemento_atual)