# Exercício 3:
# Escreva uma função em Python que receba uma matriz como entrada e retorne o maior elemento 
# presente na matriz.
import random

def maior_elemento(mat):
    maior = 0
    for i in mat:
        for b in i:
            if b > maior:
                maior = b
    return maior

matriz  = [[random.randint(1,99) for n in range(3)]for n in range(3)]

print("Matriz")
for i in range(len(matriz)):
    print(matriz[i])


print("o maior elemento da matriz é:",maior_elemento(matriz))