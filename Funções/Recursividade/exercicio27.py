# 32. Defina a função sup_listas2 que recebe como argumento uma lista de listas de números inteiros  w
# e devolve uma lista de comprimento igual a  w contendo em cada posição o supremo de cada uma das listas de  w
# na posição correspondente.

def sup_listas2(conjunto,posconjunto=0,lista_sup=[],sup=0):
    if posconjunto == len(conjunto):
        return lista_sup
    if not conjunto[posconjunto]:
        sup = float('-inf')
    else:
        for i in conjunto[posconjunto]:
            if i > sup:
                sup = i
    lista_sup.append(sup)
    
    posconjunto +=1 
    return sup_listas2(conjunto,posconjunto,lista_sup,sup=0)


print(sup_listas2([[1,2,3],[4,3,2],[],[7,7,7,7]]))