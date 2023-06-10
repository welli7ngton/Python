# Exercício 7:
# Escreva uma função em Python que receba duas matrizes como entrada e verifique se as duas 
# matrizes são iguais.

import random

def verificacao(m1,m2):

    l = len(m1) 
    c = len(m1[0])

    for i in range(l):
        for j in range(c):
            if m1[i][j] != m2[i][j]:
                return "As matrizes são diferentes"
    
    return "As matrizes são iguais"




mat1 = mat2 = [[random.randint(1,99)for _ in range(7)]for _ in range(5)]

# mat1 = [[random.randint(1,99)for _ in range(7)]for _ in range(5)]
# mat2 = [[random.randint(1,99)for _ in range(7)]for _ in range(5)]


print(verificacao(mat1,mat2))