#Problema "media_pares "
#Fazer um programa para ler um vetor de N números inteiros. Em seguida, mostrar na tela a média
#aritmética somente dos números pares lidos, com uma casa decimal. Se nenhum número par for
#digitado, mostrar a mensagem "NENHUM NUMERO PAR"

n = int(input("quantos elementos vai ter o vetor? "))

vet : [int] = [0 for x in range(n)]

pares : [int] = []

for a in range(0,n):
    vet[a] = int(input("digite um numero: "))
    if vet[a] %2 == 0:
        pares.append(vet[a])


if len(pares) == 0:
    print("NENHUM NUMERO PAR")
else:
    mediapares = sum(pares) / len(pares)
    print(f"MEDIA DOS PARES = {mediapares:.1f}")
