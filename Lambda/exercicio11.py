# 11-Escreva uma expressão lambda que retorne o menor de dois números.

def executa(fun,*args):
    return fun(*args)


l = [(1,5),(3,16),(532,670),(7394823,842)]

for i in range(len(l)):
    print(executa(lambda n1,n2: n1 if n1 < n2 else n2, l[i][0], l[i][1]))

print()
f = lambda n1,n2: n1 if n1 < n2 else n2

for i in range(len(l)):
    print(f(l[i][0], l[i][1]))