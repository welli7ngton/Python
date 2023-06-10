# Exercício 2:
# Escreva uma função em Python que receba uma matriz como entrada e retorne a transposta dessa 
# matriz.

def transposta(mat):

    transposta = [[0 for a in range(len(mat))]for b in range(len(mat[0]))]

    for i in range(len(mat)):
        for j in range(len(mat[0])):
            transposta[j][i] = mat[i][j] 
    return transposta

mat = [[n for n in range(1, 4)]for n in range(4)]

print("matriz: ")
for a in range(len(mat)):
    print(mat[a])

t = transposta(mat)

print("transposta: ")
for a in range(len(t)):
    print(t[a])