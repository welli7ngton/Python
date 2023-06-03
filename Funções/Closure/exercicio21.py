# Crie uma função chamada make_average_calculator que retorna uma função interna. A função interna deve receber 
# uma lista de números e calcular a média deles. Teste a função retornada para calcular a média de diferentes 
# listas de números.


def make_average_calculator():
    def calculo(l=[]):
        soma = 0
        for n in l:
            soma += n
        return soma/len(l)
    return calculo


a = make_average_calculator()

print(a([2,2,2,2]))
print(a([6,6,6,6]))
print(a([9,9,7,7]))
print(a([2,6,3,10]))

# saída:
# 2.0
# 6.0
# 8.0
# 5.25