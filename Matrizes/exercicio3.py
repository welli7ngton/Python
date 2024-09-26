# Problema "negativos_matriz"
# Ler dois números M e N (máximo = 10), e depois ler uma matriz MxN de números inteiros, conforme
# exemplo. Em seguida, mostrar na tela somente os números negativos da matriz.


m = int(input("digite o digite um número para M: "))
n = int(input("digite o valor de N: "))

mat = [[0 for x in range(n)] for x in range(m)]
vet = []
for a in range(0, m):
    for b in range(0, n):
        mat[a][b] = int(input(f"elemento [{a},{b}]: "))

        if mat[a][b] < 0:
            vet.append(mat[a][b])

if __name__ == "__main__":
    print("valores negativos: ")
    for a in range(0, len(vet)):
        print(vet[a])
