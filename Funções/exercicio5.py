#4- Faça um programa, com uma função que necessite de um argumento. A função retorna o valor de caractere ‘P’
#se seu argumento for positivo, e ‘N’, se seu argumento for zero ou negativo.

a = int(input("digite o argumento: "))

def verificacao(num):
    if num > 0:
        print("P")
    else:
        print("N")

verificacao(a)

