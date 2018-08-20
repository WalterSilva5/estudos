import random
import time

def bubble_sort(v):
    
    fim = len(v)
    while fim > 0:
        j = 0
        #percorrer de j até o fim atual
        while j < fim-1:
            #verificando se precisa trocar
            if v[j] > v[j+1]:
                #realizar a troca
                temp = v[j]
                v[j] = v[j+1]
                v[j+1] = temp
                
            j += 1
        
        fim -= 1

vetor = list(range(0,10000))
random.shuffle(vetor)

antes = time.time()
bubble_sort(vetor)
depois = time.time()

total = depois - antes

print("Tempo total foi: %0.2f ms" % (total * 1000))