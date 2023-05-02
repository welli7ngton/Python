#Problema "soma_linhas"
#Fazer um programa para ler dois números inteiros M e N (máximo = 10). Em seguida, ler uma matriz
#de M linhas e N colunas contendo números reais. Gerar um vetor de modo que cada elemento do vetor
#seja a soma dos elementos da linha correspondente da matriz. Mostrar o vetor gerado. 


m = int(input("digite o valor de M: "))
n = int(input("digite o valor de N: "))


mat = [[0 for x in range(n)]for x in range(m)]
vet = []

for a in range(0,m):
    print(f"digite os valores da {a + 1}a linha: ")
    for b in range(0,n):
        mat[a][b] = float(input())

    vet.append(mat[a][:])

print("vetor gerado: ")
for a in range(0, len(vet)):

    print(sum(vet[a]))
