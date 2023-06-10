# Exercício 4:
# Escreva uma função em Python que receba uma matriz como entrada e verifique se a matriz é 
# simétrica. Uma matriz é simétrica se ela for igual à sua transposta.

def verifica_simetria(mat):

    linhas = len(mat)
    colunas = len(mat[0])

    if linhas != colunas:
        return False

    transposta = [[0 for _ in range(linhas)]for _ in range(colunas)]

    for i in range(linhas):
        for j in range(colunas):
            if mat[i][j] != mat[j][i]:
                return False
    
    return True


# mat = [[x for x in range(5)]for x in range(5)]
mat = [
    [1, 2, 3],
    [2, 4, 5],
    [3, 5, 6]
]

print(verifica_simetria(mat))
