# criar programa onde o usuario digita 7 valores
# cadastrar eles em uma lista que separe os numeros pares de impares
# no final mostrar os valores pares e impares em ordem crescente

'''               JEITO 1
num = []
pares = []
impares = []

for a in range(0, 7):

    n = int(input(f"digite o {a+1}° valor: "))
    if n %2 == 0:
        pares.append(n)
    else:
        impares.append(n)
    

num.append(pares)
num.append(impares)

print(f"os valores pares foram {num[0]}")

print(f"os valores impares foram {num[1]}")'''


#                  JEITO 2

num = []
pares = []
num.append(pares)
impares = []
num.append(impares)


for a in range(0,7):

    n = int(input(f"digite o {a + 1}° valor: "))
    if n %2 == 0:
        pares.append(n)
    else:
        impares.append(n)

print(f"os valores pares foram: {num[0]}")

print(f"os valores impares foram: {num[1]}")
