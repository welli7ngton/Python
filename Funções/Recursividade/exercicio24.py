# 29. Defina a função inverteLista que recebe como argumento uma lista  we devolve a mesma lista mas 
# invertida.


def inverteLista(l,nl=[], posl=-1):
    if len(nl) == len(l):
        return nl
    else:
        nl.append(l[posl])
    
    posl += -1
    return inverteLista(l,nl,posl)

print(inverteLista([1,2,3,4,5]))

# saída:
# [5, 4, 3, 2, 1]
