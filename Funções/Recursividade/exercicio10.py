# 14. Defina a função negpos que recebe como argumento uma lista de números inteiros  w
# e devolve a diferença entre o número de números positivos e o número de números negativos de w.



def negpos(lista, pos=0, dif=0, posi=0, neg=0):

    if pos == len(lista):
        return dif
    if lista[pos] > 0:
        posi += 1
    else:
        neg += 1
    pos += 1
    dif += posi - neg
    return negpos(lista, pos, dif)

print(negpos([1,2,3,-1]))
