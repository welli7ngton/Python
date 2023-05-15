# 1. Defina a função soma_nat que recebe como argumento um número natural  n
#  e devolve a soma de todos os números naturais até  n

def soma_nat(n):
    if n == 0:
        return 0
    else:
        return n + soma_nat(n -1)
        n -= 1

a = soma_nat(5)

print(a)