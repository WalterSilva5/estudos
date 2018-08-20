x = int(input(""))
y = int(input(""))

def funcao_x_menor(x,y):
    if x<=y:        
        print(x)
        return(funcao_x_menor(x+1,y))
        
def funcao_y_menor(x,y):
    if x>=y:
        print(x)
        return(funcao_y_menor(x-1,y))

if x<=y:
    funcao_x_menor(x,y)
else:
    funcao_y_menor(x,y)
