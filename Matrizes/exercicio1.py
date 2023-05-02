#Problema "diagonal_negativos"
#Fazer um programa para ler um número inteiro N (máximo = 10) e uma matriz quadrada de ordem N
#contendo números inteiros. Em seguida, mostrar a diagonal principal e a quantidade de valores
#negativos da matriz.

n = int(input("digite n: "))

mat = [[0 for x in range(n)] for x in range(n)]

for a in range(0,n):
    for b in range(0,n):
        
        mat[a][b] = int(input("digite um número na matriz: "))
print()
diagonal = []
for a in range(0,n):
    diagonal.append(mat[a][a])
            
print("a diagonal principal é: ",diagonal)

print()
contaneg = 0
for a in range(0,n):
    for b in range(0,n):
        if mat[a][b] < 0:
            contaneg +=1

print("a quantidade de negativos da matriz é: ", contaneg)