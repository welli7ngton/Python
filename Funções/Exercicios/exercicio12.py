#Desenha moldura. Construa uma função que desenhe um retângulo usando os caracteres ‘+’ , ‘−’ e ‘|‘. 
#Esta função deve receber dois parâmetros, linhas e colunas, sendo que o valor por omissão é o valor mínimo
#igual a 1 e o valor máximo é 20. Se valores fora da faixa forem informados, eles devem ser modificados para
#valores dentro da faixa de forma elegante.


'''

+------------------------+
|                        |
|                        |
|          7x26          |
|                        |
|                        |
+------------------------+

'''

def retangulo(l,c):
    print("+" + ("-"*(c-2)) + "+")
    for a in range(l-2):
        print("|"+(" "*(c-2))+"|")
    print("+" + ("-"*(c-2)) + "+")



linhas = int(input("digite a quantidade de linhas: "))
colunas = int(input("digite a quantidade de colunas: "))

retangulo(linhas, colunas)