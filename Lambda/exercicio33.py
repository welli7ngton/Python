# Escreva uma expressão lambda que retorne o valor máximo de uma lista de dicionários com 
# base em uma determinada chave.

f = lambda lista, key: max(lista, key=lambda x: x[key])

l = [{'a': 5, 'b': 2}, {'a': 10, 'b': 7}, {'a': 3, 'b': 1}]

r = f(l, 'a')
print(r)

