# 20. Defina a função lposicoes que recebe como argumentos uma lista de números inteiros  w e um número inteiro  
# k  e devolve a lista das posições em que  k  ocorre em  w

def lposicoes(w=[],k=0,lpos=[],c=0):
    if c == len(w):
        return lpos
    
    if w[c] == k:
        lpos.append(c)
        c+=1
    else:
        c += 1
    return lposicoes(w,k,lpos,c)

print(lposicoes([1,2,3,4,2,2],2))   

