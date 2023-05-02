#Problema "dados_pessoas"
#Tem-se um conjunto de dados contendo a altura e o gênero (M, F) de N pessoas. Fazer um programa
#que calcule e escreva a maior e a menor altura do grupo, a média de altura das mulheres, e o número
#de homens. 

n = int(input("digite a quantidade de pessoas: "))

menoraltura = 100.0
maioraltura = 0

altura : [float] = [0 for x in range(n)]
genero : [str] = [0 for x in range(n)]
alturaf = []

for a in range(0,n):
    print(f"altura da {a + 1}a pessoa:")
    altura[a] = float(input())
    if altura[a] < menoraltura:
        menoraltura = altura[a]
    if altura[a] > maioraltura:
        maioraltura = altura[a]
    print(f"genero da {a + 1}a pessoa:")
    genero[a] = input()
    if genero[a] in "Ff":
        alturaf.append(altura[a])

media = sum(alturaf) /len(alturaf)

qtdM = n - len(alturaf)

print(f"Menor altura: {menoraltura:.2f}")
print(f"Maior altura: {maioraltura:.2f}")
print(f"Media das alturas das mulheres: {media:.2f}")
print(f"Numero de homens: {qtdM}")