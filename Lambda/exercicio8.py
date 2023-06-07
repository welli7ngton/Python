# 8-Escreva uma expressão lambda que verifique se um número é positivo.

def executa(fun,*args):
    return fun(*args)

l = [1,-37,4,-3,91]

print(l)
for i in range(len(l)):
    print(executa(lambda n: True if n > 0 else False,l[i]))


a = lambda n: "positivo" if n >0 else "negativo"
print(l)
for i in range(len(l)):
    print(a(l[i]))