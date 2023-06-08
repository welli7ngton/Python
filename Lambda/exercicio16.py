# 16-Escreva uma expressão lambda que retorne a soma dos elementos de uma lista.

def executa(fun,*args):
    return fun(*args)


l = [1,2,3,4,5,6,7,8,9]
l2 = [1,202,3,4,5,6,7,100,43437,-232]

print(executa(lambda x: sum(x),l))


f = lambda y: sum(y)

print(f(l2))