# 18-Escreva uma expressão lambda que conte o número de ocorrências de um determinado 
# elemento em uma lista.
l = [1,1,1,2,3,1,0,1,34,34,3,1]

f = lambda l1, e: sum(1 for item in l1 if item == e)
print(f(l,1))