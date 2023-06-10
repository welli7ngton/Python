# Exercício 1:
# Escreva uma função em Python que receba duas matrizes como entrada e retorne a soma das duas 
# matrizes. Considere que as matrizes têm o mesmo tamanho.


def soma_mat(m1,m2):
    total= 0
    for i in m1:
        for b in i:
            total += b

    for i in m2:
        for b in i:
            total += b
    
    return total

linhas = int(input("digite a quantidade de linha das matrizes: "))
colunas = int(input("digite a quantidade de coluna das matrizes: "))


m1 =[[n for n in range(1,colunas + 1)]for i in range(linhas)]

m2 =[[n for n in range(1,colunas + 1)]for i in range(linhas)]

print("matriz 1:")
for a in range(len(m1)):
    print(m1[a])
print("matriz 2:")
for a in range(len(m2)):
    print(m2[a])

print("a soma dos valores das matrizes é:",soma_mat(m1,m2))