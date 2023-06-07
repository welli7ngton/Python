# 15-Escreva uma expressão lambda que verifique se uma lista está vazia.


def executa(fun, *args):
    return(fun(*args))

listas = [[],[0,1,2],[1],["vazia"],[],[],[3,3]]

for item in listas:
    print(executa(lambda x: True if len(x) == 0 else False, item))
