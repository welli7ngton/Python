# 28-Escreva uma expressão lambda que verifique se uma lista contém apenas números.

l = [1,2,3,4,5,'1']

f = lambda x: [
    True if str(x[pos]).isdigit() else False for pos in range(len(x))
]

a = f(l)

if False in a:
    print(False)
else:
    print(True)



