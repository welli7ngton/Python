#Problema "matriz_geral"
#Ler uma matriz quadrada de ordem N (máximo = 10), contendo números reais. Em seguida, fazer as
#seguintes ações:
#a) calcular e imprimir a soma de todos os elementos positivos da matriz.
#b) fazer a leitura do índice de uma linha da matriz e, daí, imprimir todos os elementos desta linha.
#c) fazer a leitura do índice de uma coluna da matriz e, daí, imprimir todos os elementos desta coluna.
#d) imprimir os elementos da diagonal principal da matriz.
#e) alterar a matriz elevando ao quadrado todos os números negativos da mesma. Em seguida imprimir
#a matriz alterada. 

n = int(input("digite o valor de N: "))

mat = [[0 for x in range(n)]for x in range(n)]

positivos = []
diagonal = []

for a in range(n):
    for b in range(n):
        mat[a][b] = float(input(f"Elemento [{a}, {b}]: "))
        if mat[a][b] > 0:
            positivos.append(mat[a][b])

    diagonal.append(mat[a][a])

for a in range(0,n):
    print(mat[a])

print("a soma dos positivos é: ",sum(positivos))

linha = int(input("escolha uma linha: "))
print("linha escolhida: ", mat[linha])

coluna = int(input("escolha uma coluna: "))
print("coluna escolhida: ")
for a in range(0,n):
    print(mat[a][coluna], end=" ")

print("\n",)
print("os elementos da diagonal principal são:",diagonal)

for a in range(0,n):
    for b in range(0,n):
        if mat[a][b] < 0:
            mat[a][b] = (mat[a][b] * -1) ** 2

print("Matriz alterada: ")
for a in range(0,n):
    print(mat[a])
