#Problema "mais_velho"
#Fazer um programa para ler um conjunto de nomes de pessoas e suas respectivas idades. Os nomes
#devem ser armazenados em um vetor, e as idades em um outro vetor. Depois, mostrar na tela o nome
#da pessoa mais velha. 

n = int(input("digite a quantidade de pessoas: "))
nomes : [str] = [0 for x in range(n)]
idades : [int] = [0 for x in range(n)]
maioridade = 0
maisvelho = ''
for a in range(0,n):

    print(f"dados da {a + 1}a pessoa")
    nomes[a] = input("nome: ")
    idades[a] = int(input("idade: "))
    if idades[a] > maioridade:
        maioridade = idades[a]
        maisvelho = nomes[a]

print(f"pessoa mais velha: {maisvelho.capitalize()}")