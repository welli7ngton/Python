# 10-Escreva uma expressão lambda que retorne o maior de dois números.

def executa(fun,*args):
    return fun(*args)

print(executa(lambda n1,n2: n1 if n1 > n2 else n2,3,2))

print()

f = lambda n1,n2: n1 if n1 > n2 else n2

print(f(0,1))
print(f(1,2))
print(f(3,2))
print(f(3,4))
print(f(5,4))
print(f(5,6))