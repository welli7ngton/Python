#Escreva um programa que leia a idade e o primeiro nome de varias pessoas. Seu pro- ´
#grama deve terminar quando uma idade negativa for digitada. Ao terminar, seu programa
#deve escrever o nome e a idade das pessoas mais jovens e mais velhas.
c = 9999
menoridade = 200
maioridade = 0
maisnovo = ''
maisvelho = ''
for a in range(0,c):

    idade = int(input("digite sua idade: "))
    if idade < 0:
        break
    nome = input("digite seu nome: ")


    if idade > maioridade:
        maioridade = idade
        maisvelho = nome
        
    elif idade < menoridade:
        menoridade = idade
        maisnovo = nome
        


print(f"o nome da pessoa mais velha é {maisvelho} e sua idade é: {maioridade}")
print(f"o nome da pessoa mais nova é {maisnovo} e sua idade é: {menoridade}")



