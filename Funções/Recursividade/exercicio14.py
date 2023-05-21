# 18. Defina a função supremo que recebe como argumento uma lista de números inteiros  w
# e devolve o supremo de  w Note que o supremo do conjunto vazio é  − ∞ Para representar

from math import inf


def supremo(lista, pos=0, sup= 0):
    if len(lista) == 0:
        sup = - inf
        return sup

    if pos == len(lista):
        return sup

    else:
        if lista[pos] > sup:
            sup = lista[pos]
            
            return supremo(lista, pos + 1, sup)
        else:
            return supremo(lista, pos + 1, sup)


print(supremo([3,2,1]))