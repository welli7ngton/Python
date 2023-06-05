# 26. Defina a função mapeia que recebe como argumentos uma função f e uma lista  w e devolve a lista que 
# resulta de aplicar  f a cada um dos elementos de  w


def suc(x):
    return x + 1


def mapeia(suc,l=[],n_l=[],pos=0):
    if pos == len(l):
        return n_l
    
    n_l.append(suc(l[pos]))
    return mapeia(suc,l,n_l,pos + 1) 


print(mapeia(suc,[]))
print(mapeia(suc,[0,1,2,3,4,5]))
