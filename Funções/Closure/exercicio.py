# crie uma função que duplica, triplica e quadriplica um numero que é dado como argumento de função usando closure

def fun(x):
    def mult(y):
        return x * y
    return mult


for a in range(0,10):
    resultado = fun(4)
    print(f"{4} x {a} = {resultado(a)}")

print()

for a in range(0,10):
    resultado = fun(7)
    print(f"7 x {a} = {resultado(a)}")

# saída:
# 4 x 0 = 0
# 4 x 1 = 4 
# 4 x 2 = 8 
# 4 x 3 = 12
# 4 x 4 = 16
# 4 x 5 = 20
# 4 x 6 = 24
# 4 x 7 = 28
# 4 x 8 = 32
# 4 x 9 = 36

# 7 x 0 = 0 
# 7 x 1 = 7 
# 7 x 2 = 14
# 7 x 3 = 21
# 7 x 4 = 28
# 7 x 5 = 35
# 7 x 6 = 42
# 7 x 7 = 49
# 7 x 8 = 56
# 7 x 9 = 63