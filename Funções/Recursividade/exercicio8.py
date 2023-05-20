#12. Defina a função todos_imparesQ que recebe como argumento uma lista de números inteiros  w
# e devolve True se  w contém apenas números ímpares e False em caso contrário.


def todos_imparesQ(lista, pos=0):
    if pos == len(lista):
        return True
    if lista[pos] %2 != 0:
        pos += 1
        return todos_imparesQ(lista,pos)
    else:
        return False


print(todos_imparesQ([1,2,3,4,5]))