# 3 - Crie uma função chamada calculate_power que recebe um número x e retorna uma função interna. A função 
# interna deve receber um número n e retornar x elevado a n. Teste a função retornada para calcular potências.

def calcula_elevado(x):
    def elevado(n):

        return x**n

    return elevado

a = calcula_elevado(int(input("Digite o numero para calcular a potenciação: ")))

p = int(input("Digite a potência: "))

print(a(p))

