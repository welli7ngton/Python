# crie uma função que duplica, triplica e quadriplica um numero que é dado como argumento de função usando closure

def fun(x):
    def mult(y):
        return x * y
    return mult

n = int(input("Digite um número: "))

print(f"Tabuada de {n}:")

for a in range(0,10):
    resultado = fun(n)
    print(f"{n} x {a} = {resultado(a)}")