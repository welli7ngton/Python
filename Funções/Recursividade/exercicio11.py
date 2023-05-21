#15. Defina a função indices_impar que recebe como argumento uma lista de números inteiros  w e devolve a lista dos 
# elementos de  w em posições de índice ímpar. Recorde que a primeira posição de uma lista tem índice 0, que é um número par.

impares = []

def indices_impar(lista, pos=0):
    if pos == len(lista):
        return impares

    if pos %2 != 0:
        impares.append(lista[pos])
        pos += 1
        return indices_impar(lista, pos)
    else:
        pos += 1
        return indices_impar(lista, pos)
    
print(indices_impar([1,2]))