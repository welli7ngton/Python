# 7-Escreva uma expressão lambda que verifique se uma palavra começa com uma 
# determinada letra.

def executa(fun,*arg):
    return fun(*arg)

print(executa(lambda p,l: True if p[0].lower() == l.lower() else False,"wellington","a"))


f = lambda palavra, letra: True if palavra[0].lower() == letra.lower() else False

print(f("wellington","x"))
print(f("Carro","c"))
print(f("bola","B"))