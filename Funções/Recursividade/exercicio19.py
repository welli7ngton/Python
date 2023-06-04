# 23. Defina a função apaga1 que recebe como argumentos uma lista de números inteiros  w e um número inteiro  k
# e devolve a lista que resulta de apagar de  w a primeira ocorrência de  k (caso exista).


def apaga1(w=[],k=0,c=0,w2=[]):
    if c == len(w):
        return w2
    
    if w[c] == k:
        w.remove(w[c])
        k = None
        w2.append(w[c])
    else:
        w2.append(w[c])
    c += 1
    return apaga1(w,k,c,w2)

print(apaga1([1,2,3,4,3,2,1],3))


        
        


