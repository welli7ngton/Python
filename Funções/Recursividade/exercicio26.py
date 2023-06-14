# 31. Defina a função sup_listas1 que recebe como argumento uma lista de listas de números inteiros  w
# e devolve o supremo de  w

def sup_listas1(conjunto,posconjunto=0,sup=0):
    if posconjunto == len(conjunto):
        return sup
    
    for i in conjunto[posconjunto]:
        if i > sup:
            sup = i
    posconjunto +=1 
    return sup_listas1(conjunto,posconjunto,sup)

print(sup_listas1([[1,2,3],[2,3,4],[2]]))
print(sup_listas1([[7,3,2],[],[1,2,3]]))