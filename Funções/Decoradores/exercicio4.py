# 4- Escreva uma função decoradora chamada memoriza que armazene em cache o resultado de uma função 
# para os mesmos argumentos de entrada. A próxima chamada com os mesmos argumentos não deve executar 
# novamente a função, mas retornar o resultado armazenado em cache.

def memoriza(fun):
    cache = []
    resultados = []
    def execucao(*args):
        nonlocal cache, resultados
        if args in cache:
            indice = cache.index(args)
            return f'Resultado ja processado = {resultados[indice]}'

        else:
            cache.append((args))
            resultados.append(fun(*args))
        # print(*cache)
        return fun(*args)
    return execucao


@memoriza
def soma(x,y):
    return x+y



print(soma(3,3))
print(soma(4,4))
print(soma(3,3))
print(soma(2,2))
print(soma(1,5))
print(soma(2,2))
print(soma(4,4))