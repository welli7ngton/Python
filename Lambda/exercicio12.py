# 12-Escreva uma expressão lambda que calcule o produto de dois números.


def executa(fun,*args):
    return fun(*args)

print(executa(lambda n1,n2: n1*n2,3,4))


f = lambda x,y: x*y

print(f(2,5))