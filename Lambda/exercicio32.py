# Escreva uma expressão lambda que calcule a soma dos quadrados dos números positivos de uma lista.

l = [-2, -1, 0, 1, 2, 3, 4, 5]

f = lambda l1: sum(x**2 for x in l1 if x > 0)

print(f(l))