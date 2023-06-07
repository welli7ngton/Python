# 14-Escreva uma expressão lambda que retorne a raiz quadrada de um número.

def executa(fun,*args):
    return fun(*args)

l = [i for i in range(31)]

for a in range(len(l)):
    print(f"o quadrado de {l[a]} é = ",executa(lambda x: x**2, l[a]))
