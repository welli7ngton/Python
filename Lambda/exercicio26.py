# 26-Escreva uma expressão lambda que concatene duas strings.

def executa(fun,*args):
    return fun(*args)



a = "wellington"
b = "silva"

print(executa(lambda x,y: x+y,a,b))

a = "wellington"
b = "almeida"

f = lambda s1,s2: s1+s2

print(f(a,b))