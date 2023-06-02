# Crie uma função chamada make_exponentiator que recebe um número x como argumento e retorna uma função interna. 
# A função interna deve receber um número n e retornar x elevado à potência n. Teste a função retornada para 
# calcular diferentes potências.

def make_exponentiator(x):
    def power(n):
        return x**n
    return power

r = make_exponentiator(2)


print(r(1))
print(r(2))
print(r(3))
print(r(4))
print(r(5))
print(r(6))
print(r(7))
print(r(8))
print(r(9))
print(r(10))