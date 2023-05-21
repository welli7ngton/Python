# 16. Defina a função escolhe_pares que recebe como argumento uma lista de números inteiros  w
#  e devolve a lista dos elementos pares de  w

novalista =[]

def escolhe_pares(lista, pos=0):
    if pos == len(lista):
        return novalista
    if lista[pos] %2 == 0:
        novalista.append(lista[pos])
        pos += 1
        return escolhe_pares(lista, pos)
    else:
        pos += 1
        return escolhe_pares(lista, pos)


print(escolhe_pares([1,3,5,7,9]))

