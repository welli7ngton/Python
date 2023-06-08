# 19-Escreva uma expressão lambda que filtre os números pares de uma lista.

l = [1,2,3,4,5,6,7,8,9]


f = lambda l1: list(filter(lambda x: x % 2 == 0, l1))

print(f(l))