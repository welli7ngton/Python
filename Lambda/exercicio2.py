# 2-Escreva uma expressão lambda que calcule o quadrado de um número.

def executa(funcao,num):
    return funcao(num)

for i in range(0,7):
    print(executa(lambda x: x**2, i+1))

print()

a = lambda x: x**2

for i in range(1,8):
    print(a(i))