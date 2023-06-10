# Exercício 4:
# Escreva uma função em Python que receba uma matriz como entrada e verifique se a matriz é 
# simétrica. Uma matriz é simétrica se ela for igual à sua transposta.

def verifica_simetria(mat):

    linhas = len(mat)
    colunas = len(mat[0])

    transposta = [[0 for _ in range(linhas)]for _ in range(colunas)]

    for i in range(linhas):
        for j in range(colunas):
            transposta[j][i] = mat[i][j]
    


mat = [[0 for x in range(5)]for x in range(2)]


