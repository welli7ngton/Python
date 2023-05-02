#Escreva um programa que recebe do usuario uma string S, um caractere C, e uma 
#posicao I e devolve o ındice da primeira posicao da string onde foi encontrado o caractere 
#C. A procura deve comecar a partir da posicao I.



s = input("digite uma string S: ")
c = input("digite o caractere C: ")
i = int(input("digite a posição I: "))

indice = s.find(c, i)

if indice == -1:
    print(f"O caractere {c} não foi encontrado a partir da posição {i}.")
else:
    print(f"O índice onde foi encontrado {c} é: {indice}")