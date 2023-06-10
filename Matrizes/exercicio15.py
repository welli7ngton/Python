# Exercício 8:
# Escreva uma função em Python que receba uma matriz como entrada e retorne uma nova matriz com 
# os elementos ordenados em ordem crescente.

import random 

def ordena(mat):
    ordenado = []
    for i in mat:
        for j in i:
            ordenado.append(j)
    c = 0
    ordenado = sorted(ordenado)
    
    for a in range(len(mat)):
        for b in range(len(mat[0])):
            mat[a][b] = ordenado[c]
            c += 1
        

    return mat


mat1 = [[random.randint(10,99)for _ in range(5)]for _ in range(5)]

print("Matriz:")
for i in mat1:
    print(i)

print()
mat1 = ordena(mat1)
print("Matriz ordenada:")
for i in mat1:
    print(i)