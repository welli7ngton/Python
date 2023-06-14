# 34. Defina a função intercala que recebe como argumentos duas listas  w1 e  w2 e devolve a lista resultante de 
# intercalar os elementos de  w1 com os de  w2

def intercala(l1,l2,l3=[],pos=0):
    if max(len(l1),len(l2)) == pos:
        return l3
    try:
        l3.append(l1[pos])
        l3.append(l2[pos])
    except IndexError:
        if len(l1) > len(l2):
            for i in l1:
                l3.append(i)
        else:
            for i in l2:
                l3.append(i)
        return l3
    pos += 1
    return intercala(l1,l2,l3,pos)

print(intercala([2,4],[1,3,5,7,9]))