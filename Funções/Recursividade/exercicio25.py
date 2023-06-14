# 30. Defina a função lista_igualQ que recebe como argumentos duas lista e devolve True se as listas forem iguais 
# e False em caso contrário. Não pode usar a comparação == entre listas.


def lista_igualQ(l1,l2, pos=0,result=None):
    if len(l1)!=len(l2):
        return False
    if pos == len(l1) or result == False:
        return result
    if l1[pos]==l2[pos]:
        pos +=1
        result = True
    else:
        result = False
        pos += 1

    return lista_igualQ(l1,l2,pos,result)


print(lista_igualQ([1,2,3],[1,2,3]))
print(lista_igualQ([1,2,3],[1,3,3]))
print(lista_igualQ([1,2],[1,2,3]))
print(lista_igualQ([1,2,3],[1,2]))