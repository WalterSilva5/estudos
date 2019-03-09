import random 
vetor = list(range(10))
random.shuffle(vetor)
alvo = 5
global pos
pos = 0
print(list(range(10)))
print(vetor)
def buscaSeq(vetor, alvo, pos):
    if pos == len(vetor):
        return -1
    elif vetor[pos] == alvo:
        print(pos)
    else:
        pos+=1
        buscaSeq(vetor, alvo, pos)

buscaSeq(vetor, alvo, pos)
