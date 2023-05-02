#2- Faça um programa para imprimir:
#    1
#    1   2
#    1   2   3
#    .....
#    1   2   3   ...  n
#   para um n informado pelo usuário. Use uma função que receba um valor n inteiro imprima até a n-ésima linha.


n = int(input("digite o valor de n: "))

def linhas2(n):

    linhas = []
    num = 1
    for a in range(n):
        linhas.append(num)
        num += 1
        print(linhas)
    return(linhas)

linhas2(n)
