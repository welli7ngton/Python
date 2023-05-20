#11. Defina a função contem_par que recebe como argumento uma lista de números inteiros  w
#e devolve True se  w contém um número par e False em caso contrário.

def contem_par(lista, pos=0):

    if pos >= len(lista):
        return False
    num = lista[pos]
    if num %2 == 0:
        return True
    else:
        pos += 1
        return contem_par(lista, pos)

print(contem_par([]))