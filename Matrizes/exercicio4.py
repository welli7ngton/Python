#Problema "cada_linha"
#Ler um inteiro N e uma matriz quadrada de ordem N (máximo = 10). Mostrar qual o maior elemento
#de cada linha. Suponha não haver empates. 


n = int(input("digite o valor de N: "))

mat = [[0 for x in range(n)]for x in range(n)]

vetmaior = [0 for x in range(n)]

for a in range(0,n):
    for b in range(0,n):
        mat[a][b] = int(input(f"elemento [{a} , {b}]: "))

        if mat[a][b] > vetmaior[a]:
            vetmaior[a] = mat[a][b]
    
for a in range(0, n):
    print("os maiores numeros de cada linha são: ",vetmaior[a])