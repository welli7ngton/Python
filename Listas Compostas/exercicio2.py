# criar programa onde o usuario digita 7 valores
# cadastrar eles em uma lista que separe os numeros pares de impares
# no final mostrar os valores pares e impares em ordem crescente

'''                JEITO FÁCIL
num = []
pares = []
impares = []

for a in range(0, 7):

    n = int(input(f"digite 0 {a}o valor: "))
    if n %2 == 0:
        pares.append(n)
    else:
        impares.append(n)
    

num.append(pares)
num.append(impares)

print(f"os valores pares foram {num[0]}")

print(f"os valores impares foram {num[1]}")'''


#                  JEITO MAIS COMPLICADO UMA COISINHA

num = []
pares = []
num.append(pares)
impares = []
num.append(impares)


for a in range(0,7):

    n = int(input(f"digite 0 {a + 1}o valor: "))
    if n %2 == 0:
        pares.append(n)
    else:
        impares.append(n)

print(f"os valores pares foram: {num[0]}")

print(f"os valores impares foram: {num[1]}")

