# 21. Defina a função pos_max que recebe como argumento uma lista de números inteiros e devolve o índice da 
# primeira posição onde ocorre o máximo da lista. No caso da lista vazia, devolve -1.


def pos_max(l=[],maior=0, pos_maior=0, c=0):
    if len(l) == 0:
        return -1
    if c == len(l):
        return pos_maior
    if l[c] > maior:
        maior = l[c]
        pos_maior = c
        c += 1
    else:
        c += 1
    return pos_max(l,maior,pos_maior,c)

print(pos_max([1,5,3,4,5,4,3]))