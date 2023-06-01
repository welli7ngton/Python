# crie uma função que duplica, triplica e quadriplica um numero que é dado como argumento de função usando closure

def fun(x):
    def mult(y):
        return x * y
    return mult

duplica = fun(2)
triplica = fun(3)
quadriplica = fun(4)

print(duplica(2))
print(triplica(2))
print(quadriplica(2))