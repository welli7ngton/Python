# 19. Defina a função conta que recebe como argumentos uma lista de números inteiros  w e um número inteiro  k  e 
# devolve o número de vezes que  k  ocorre em  w


def conta(l=list,k=0,c=0,qtd=0):

    if c == len(l):
        return qtd
    else:
        if k == l[c]:
            qtd += 1
        
            l[c] = 0
            c += 1
        else:
            c +=1

        return conta(l,k,c,qtd)

print(conta([1,2,3,2,1,2],2))
        