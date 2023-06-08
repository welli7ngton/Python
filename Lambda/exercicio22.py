# 22-Escreva uma expressão lambda que filtre os números negativos de uma lista.

l =[-1,-2,-3,4,5,6,-7]


f = lambda l1: list(filter(lambda x: x < 0, l1))


print(f(l))