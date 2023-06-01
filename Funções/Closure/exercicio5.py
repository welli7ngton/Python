# Crie uma função chamada make_adder que recebe um número x e retorna uma função interna. A função interna deve 
# receber um número n e retornar a soma de x e n. Teste a função retornada para somar diferentes números a um 
# valor fixo.


def faz_soma(x):

    def soma(n):
        return x + n
    
    return soma

a = faz_soma(10)

print(a(10)) # saída = 20