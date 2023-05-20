#13. Defina a função pertenceQ que recebe como argumentos uma lista de números inteiros  w
# e um número inteiro  n e devolve True se  n ocorre em  w e False em caso contrário.

def pertenceQ(lista, n, pos=0):
    if pos == len(lista):
        return False
    
    num = lista[pos]
    if num == n:
        return True
    else:
        pos += 1
        return pertenceQ(lista, n, pos)

print(pertenceQ([1,2,3],4))