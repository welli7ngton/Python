# 5-Escreva uma expressão lambda que retorne o valor absoluto de um número.


def executa(fun,arg):
    return fun(arg)

l = [0,5,-5,7,-7,-1,1]

for i in range(0,len(l)):
    print(executa(lambda x: x * -1 if x < 0 else x , l[i]))

print()

a = lambda x: x * -1 if x < 0 else x

for i in range(0,len(l)):
    print(a(l[i]))
