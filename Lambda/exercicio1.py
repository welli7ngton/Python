# 1-Escreva uma expressão lambda que retorne o dobro de um número.



def executa(funcao,x):
    return funcao(x)

for i in range(1,8):
    print(executa(lambda y: y*2,i))

print()

a = lambda x: x*2

for i in range(1,8):
    print(a(i))