# 33. Defina a função permutacao que recebe como argumentos duas listas  w1 e  w2 e devolve True se  w1 for uma 
# permutação de  w2 e False em caso contrário.

def permutacao(l1,l2,pos=0):
    if len(l1) != len(l2):
        return False
    if len(l1) == pos:
        return True
    for i in l2:
        if i == l1[pos]:
            pos += 1
            return permutacao(l1,l2,pos)
    return False

print(permutacao([1,2,3],[1,2,4]))
print(permutacao([1,2,3],[2,3,1]))
print(permutacao([1,1,1,2,3],[1,2,3]))