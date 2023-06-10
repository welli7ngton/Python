# Exercício 5:
# Escreva uma função em Python que receba uma matriz como entrada e retorne a soma de todos os 
# elementos da matriz.
import random

def soma(mat):
    soma = 0
    for i in mat:
        for j in i:
            soma += j
    
    return soma

mat = [[random.randint(1,99)for _ in range(4)]for _ in range(4)]

for i in mat:
    print(i)

print("A soma dos elementos da matriz é:", soma(mat))