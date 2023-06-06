# 4-Escreva uma expressão lambda que verifique se um número é ímpar.
import time

def make_timer(inicio=0, fim=0):
    
    def contador():       
        fim = time.perf_counter()
        tempo = fim - inicio
        return  tempo
    inicio = time.perf_counter()
    return contador

def executa(fun,arg):
    return fun(arg)


p1 = p2 = zero = 0
while zero < 10:
    c = make_timer()
    for i in range(1,8):
        print(executa(lambda x: f"{x} é impar" if x%2 != 0 else f"{x} não é impar",i))
    c1 = c()

    print()

    c = make_timer()
    a = lambda y: f"{y} é impar" if y%2 != 0 else f"{y} não é impar"
    for i in range(1,8):
        print(a(i))
    c2 = c()

    if c1 > c2:
        
        p2 += 1
    else:
        
        p1 += 1
    zero += 1

print()

print(f"P1 = {p1}")
print(f"P2 = {p2}")


'''
resultados: 
p2,...,p2,p2,p2,...,...,...,p2,p2,

segundo método para usar expressões lambda traz resultados mais rápido, porém não significantes
'''