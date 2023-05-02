# matriz 3x3



# minha_matriz: [[tipo]] = [[0 for x in range(numero_de_colunas)] for x in range(numero_de_linhas)]



mat : [[int]] = [[0 for x in range(3)] for x in range(3)]


for a in range(0,3):
    for b in range(0,3):
        mat[a][b] = int(input("digite um número: "))




for a in range(0,3):
    print(mat[a])