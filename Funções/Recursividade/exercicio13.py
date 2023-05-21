#17. Defina a função retira_negativos que recebe como argumento uma lista de números inteiros  w
#  e devolve a lista resultante de retirar todos os números negativos de  w

lista2 = []
def retira_negativos(lista, pos=0):
    if pos == len(lista):
        return lista2
    
    if lista[pos] < 0:
        pos += 1
        return retira_negativos(lista, pos)
    else:
        lista2.append(lista[pos])
        pos +=1
        return retira_negativos(lista, pos)

print(retira_negativos([1,-2,-3,7,0]))