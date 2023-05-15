#Escreva uma função chamada right_justify, que receba uma string chamada s como parâmetro e exiba a string com 
#espaços suficientes à frente para que a última letra da string esteja na coluna 70 da tela:



def direita_justificado(s):

    tam = len(s)
    espaco = " " * (70 - tam)
    novas = espaco + s

    print(novas)

d = input("digite a palavra: ")


direita_justificado(d)
