# 22. Defina a função car_pares que recebe como argumento uma lista de números inteiros  w e devolve uma lista com 
# True nas posições onde ocorre em  w um número par e False nas outras.

def car_par(l=[],c=0,nova_l=[]):
    if c == len(l):
        return nova_l
    else:
        if l[c] %2 == 0:
            nova_l.append(True)
            c += 1
        else:
            nova_l.append(False)
            c += 1
    
    return car_par(l,c,nova_l)

print(car_par([]))