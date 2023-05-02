#Escreva um programa que leia a idade e o primeiro nome de varias pessoas. Seu pro- ´
#grama deve terminar quando uma idade negativa for digitada. Ao terminar, seu programa
#deve escrever o nome e a idade das pessoas mais jovens e mais velhas.

c = 9999

menoridade = 200
maioridade = 0

maisnovo = ''
maisvelho = ''

for a in range(0,c):
        
    dado = str(input("digite sua idade e nome: ")).strip()

    lista = dado.split(' ') 

    idade = int(lista[0])
    nome = lista[1]

    if idade < 0:
        break

    if idade < menoridade:
        menoridade = idade
        maisnovo = nome

    if idade > maioridade:
        maioridade = idade
        maisvelho = nome
    print(maioridade)

print(f"a o mais velho é {maisvelho} e sua idade é: {maioridade}")

print(f'o mais novo é {maisnovo} e sua idade é: {menoridade}')