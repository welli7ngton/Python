# Exercício 6:
# Escreva uma função em Python que receba uma matriz quadrada como entrada e retorne a diagonal 
# principal da matriz.

import random

def diagonal_p(mat):
    if len(mat) != len(mat[0]):
        return "Não é uma matriz quadrada, logo não tem diagonal principal"
    
    diagonal = []
    cont = 0
    for i in mat:
        diagonal.append(i[cont])
        cont += 1

    return diagonal

mat = [[random.randint(1,99)for _ in range(7)]for _ in range(5)]

for i in mat:
    print(i)

print("A diagonal principal é:", diagonal_p(mat))
