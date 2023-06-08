# 17-Escreva uma expressão lambda que retorne a média dos elementos de uma lista.


def executa(fun,*args):
    return fun(*args)


l = [5,5,5,5,5]
l2 = [5,5,5,5,5,6]
print(executa(lambda x: sum(x)/len(x),l))


f = lambda y: sum(y)/len(y)

print(f(l2))