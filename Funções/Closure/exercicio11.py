# Escreva uma função chamada make_average_counter que retorna uma função interna. A função interna deve receber 
# um número como argumento e calcular a média dos números fornecidos até o momento, além de contar quantos 
# números foram fornecidos. Teste a função retornada para calcular a média e contar os números corretamente.

def make_average_counter(nums = list()):   
    def counter(num):
        nums.append(num)
        return [sum(nums)/len(nums), len(nums)]
    return counter

r = make_average_counter()

print(r(8))
print(r(6))
print(r(10))
print(r(12))
print(r(4))
print(r(2))

# saída:
# [8.0, 1]
# [7.0, 2]
# [8.0, 3]
# [9.0, 4]
# [8.0, 5]
# [7.0, 6]