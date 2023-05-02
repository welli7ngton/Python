#Problema "soma_matrizes"
#Fazer um programa para ler duas matrizes de números inteiros A e B, contendo de M linhas e N colunas
#cada (M e N máximo = 10). Depois, gerar uma terceira matriz C onde cada elemento desta é a soma
#dos elementos correspondentes das matrizes originais. Imprimir na tela a matriz gerada. 


m = int(input("quantas linhas a matriz vai ter: "))
n = int(input("quantas colunas a matriz vai ter "))

A = [[0 for x in range(n)]for x in range(m)]
B = [[0 for x in range(n)]for x in range(m)]
C = [[0 for x in range(n)]for x in range(m)]

print("digite os valores da matriz A: ")
for a in range(0,m):
    for b in range(0,n):
        A[a][b] = int(input(f"Elemento [{a},{b}]"))

print("digite os valores da matriz B: ")
for a in range(0,m):
    for b in range(0,n):
        B[a][b] = int(input(f"Elemento [{a},{b}]"))

print("matriz soma: ")
for a in range(0,m):
    for b in range(0,n):
        C[a][b] = A[a][b] + B[a][b]

    print(C[a])