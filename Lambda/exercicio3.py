# 3-Escreva uma expressão lambda que verifique se um número é par.

def executa(fun,arg):
    return fun(arg)

for i in range(0,7):
    print(executa(lambda x: f"{x} é par" if x%2 == 0 else f"{x} não é par", i+1))

print()

a = lambda x: "par" if x%2 == 0 else "não é par"

for i in range(0,7):
    print(i+1, "=" ,a(i+1))