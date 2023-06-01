# Escreva uma função chamada make_multiplier_sequence que recebe uma lista de números como argumento e retorna 
# uma função interna. A função interna deve iterar pela lista e multiplicar cada elemento pelo número fornecido. 
# Teste a função retornada para multiplicar todos os números da lista por um valor específico.

def faz_mult(lista):

    def mult(x):

        r = 0
        for n in lista:
            r += n * x
        return r
    return mult
a = faz_mult([1,2,3])

print(a(2)) # saída = 12
    