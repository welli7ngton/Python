#Problema "numeros_pares"
#Faça um programa que leia N números inteiros e armazene-os em um vetor. Em seguida, mostre na
#tela todos os números pares, e também a quantidade de números pares. 


n = int(input("quantos numeros voce vai digitar? "))

vet : [int] = [0 for x in range(n)]
vetpares = []
for a in range(0,n):
    vet[a] = int(input("digite um numero: "))
    if vet[a] %2 == 0:
        vetpares.append(vet[a])

print("Numeros Pares: ")
print(vetpares)
print(f"Quantidades de pares: {len(vetpares)}")