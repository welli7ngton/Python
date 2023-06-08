# 25-Escreva uma expressão lambda que ordene uma lista em ordem decrescente.

l = [2,6,4,3,9,8,1,5,7]


f = lambda x: x.sort(reverse=True) or x

print(f(l))