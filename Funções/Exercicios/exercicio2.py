#1- Faça um programa para imprimir:
#    1
#    2   2
#    3   3   3
#    .....
#    n   n   n   n   n   n  ... n
#   para um n informado pelo usuário. Use uma função que receba um valor n inteiro e imprima até a n-ésima linha.

# input da variavel n pra receber quantas linhas o programa vai mostrar
n = int(input("digite o valor de n: "))

# criação da função:
def linhasn(n):

    # lista pra receber a contagem
    linha = []
    
    # variavel pra preencher a lista
    num = 1

    #for para aumentar o tamanho da lista 'linha' até 'n'
    for a in range(0,n):
        linha.append(num)

        # for para reencher toda a linha com o número da linha como a questão pede
        for a in range(0,len(linha)):
            linha[a] = num 
        
        # somando 1 à num pra passar pra proxima linha
        num += 1
        print(linha)


linhasn(n)

    