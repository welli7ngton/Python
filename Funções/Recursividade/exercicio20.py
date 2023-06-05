# 24. Defina a função apaga que recebe como argumentos uma lista de números inteiros  w
# e um número inteiro  k e devolve a lista que resulta de apagar de  w todas as ocorrências de  k


def apaga(l=[],k=0,pos=0,n_l=[]):
    if k not in l:
        return l
    if pos == len(l):
        return n_l
    

    if l[pos] != k:
        n_l.append(l[pos])
        pos +=1
    else:
        pos +=1 
    
    return apaga(l,k,pos,n_l)

print(apaga([1,2,3,4,3,2,1],3))
print(apaga([1,2,3,4,3,2,1],5))
print(apaga([],3))

# saída:
# [1, 2, 4, 2, 1]
# [1, 2, 3, 4, 3, 2, 1]
# []