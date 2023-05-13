#Problema "alturas"
#Fazer um programa para ler nome, idade e altura de N pessoas, conforme exemplo. Depois, mostrar na
#tela a altura média das pessoas, e mostrar também a porcentagem de pessoas com menos de 16 anos,
#bem como os nomes dessas pessoas caso houver. 

'''qtdpessoas = int(input("quantas pessoas serão cadastradas? "))
somaalturas = 0
menor16 = 0
nome : [str] = [0 for x in range(qtdpessoas)]
idade : [int] = [0 for x in range(qtdpessoas)]
altura : [float] = [0 for x in range(qtdpessoas)]
nomes16 = []

for a in range(0, qtdpessoas):
    nome[a] = input("digite seu nome: ")
    idade[a] = input("digite sua idade: ")
    altura[a] = input("digite sua altura: ")
    somaalturas += float(altura[a])

media = somaalturas / qtdpessoas              

for i in range(0, qtdpessoas):
    if int(idade[i]) < 16:
        menor16 += 1
        nomes16.append(nome[i])
    
menor16 *= 100
percent16 = menor16 /qtdpessoas

print(f"A altura média é: {media:.2f}")
print(f"a pordentagem de idades menores que 16 anoe é {percent16:.1f}%:")
for i in range(0,len(nomes16)):
    print(nomes16[i])
    qtdpessoas = int(input("quantas pessoas serão cadastradas? "))
somaalturas = 0
menor16 = 0
nome : [str] = [0 for x in range(qtdpessoas)]
idade : [int] = [0 for x in range(qtdpessoas)]
altura : [float] = [0 for x in range(qtdpessoas)]
nomes16 = []

for a in range(0, qtdpessoas):
    nome[a] = input("digite seu nome: ")
    idade[a] = input("digite sua idade: ")
    altura[a] = input("digite sua altura: ")
    somaalturas += float(altura[a])

media = somaalturas / qtdpessoas              

for i in range(0, qtdpessoas):
    if int(idade[i]) < 16:
        menor16 += 1
        nomes16.append(nome[i])
    
menor16 *= 100
percent16 = menor16 /qtdpessoas

print(f"A altura média é: {media:.2f}")
print(f"a pordentagem de idades menores que 16 anoe é {percent16:.1f}%:")
for i in range(0,len(nomes16)):
    print(nomes16[i])qtdpessoas = int(input("quantas pessoas serão cadastradas? "))
somaalturas = 0
menor16 = 0
nome : [str] = [0 for x in range(qtdpessoas)]
idade : [int] = [0 for x in range(qtdpessoas)]
altura : [float] = [0 for x in range(qtdpessoas)]
nomes16 = []

for a in range(0, qtdpessoas):
    nome[a] = input("digite seu nome: ")
    idade[a] = input("digite sua idade: ")
    altura[a] = input("digite sua altura: ")
    somaalturas += float(altura[a])

media = somaalturas / qtdpessoas              

for i in range(0, qtdpessoas):
    if int(idade[i]) < 16:
        menor16 += 1
        nomes16.append(nome[i])
    
menor16 *= 100
percent16 = menor16 /qtdpessoas

print(f"A altura média é: {media:.2f}")
print(f"a pordentagem de idades menores que 16 anoe é {percent16:.1f}%:")
for i in range(0,len(nomes16)):
    print(nomes16[i])qtdpessoas = int(input("quantas pessoas serão cadastradas? "))
somaalturas = 0
menor16 = 0
nome : [str] = [0 for x in range(qtdpessoas)]
idade : [int] = [0 for x in range(qtdpessoas)]
altura : [float] = [0 for x in range(qtdpessoas)]
nomes16 = []

for a in range(0, qtdpessoas):
    nome[a] = input("digite seu nome: ")
    idade[a] = input("digite sua idade: ")
    altura[a] = input("digite sua altura: ")
    somaalturas += float(altura[a])

media = somaalturas / qtdpessoas              

for i in range(0, qtdpessoas):
    if int(idade[i]) < 16:
        menor16 += 1
        nomes16.append(nome[i])
    
menor16 *= 100
percent16 = menor16 /qtdpessoas

print(f"A altura média é: {media:.2f}")
print(f"a pordentagem de idades menores que 16 anoe é {percent16:.1f}%:")
for i in range(0,len(nomes16)):
    print(nomes16[i])'''
