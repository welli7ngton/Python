# 21-Escreva uma expressão lambda que filtre os números positivos de uma lista.

l = [2,-1,-2,-3,-4,1]

f = lambda l1: list(filter(lambda x: x > 0, l1))

print(f(l))