# Escreva uma função chamada make_multiplier_of que recebe um número x e retorna uma função interna. A função 
# interna deve receber um número n e retornar o resultado da multiplicação entre x e n. Teste a função retornada 
# para multiplicar diferentes números por um valor fixo.

def multiplica(x):

    def multiplicador(y):

        return x * y
    return multiplicador



r = multiplica(2)

print(r(2)) # saída = 4