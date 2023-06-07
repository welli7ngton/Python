# 9-Escreva uma expressão lambda que verifique se um número é negativo.

def executa(fun,*args):
    return fun(*args)

l = [1,-37,4,-3,91]
print(l)
for i in range(len(l)):
    print(executa(lambda x: True if x < 0 else False, l[i]),end="|")
print()

print()
f = lambda x: f"{l[i]} é negativo" if x < 0 else f"{l[i]} não é negativo"
for i in range(len(l)):
    print(f(l[i]),sep=" ")