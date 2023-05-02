#Problema "acima_diagonal"
#Ler um inteiro N (máximo = 10) e uma matriz quadrada de ordem N contendo números inteiros.
#Mostrar a soma dos elementos acima da diagonal principal. 

n = int(input("digite o valor de N: "))

mat = [[0 for x in range(0,n)]for x in range(n)]

soma = 0

for a in range(0,n):
    for b in range(0,n):
        mat[a][b] = int(input(f"Elemento [{a}, {b}]: "))

for a in range(0,n):
    for b in range(a+1,n):
        soma += mat[a][b]
  
print("A soma dos elementos acima da diagonal principal é: ",soma)