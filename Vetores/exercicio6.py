#Problema "soma_vetores"
#Faça um programa para ler dois vetores A e B, contendo N elementos cada. Em seguida, gere um
#terceiro vetor C onde cada elemento de C é a soma dos elementos correspondentes de A e B. Imprima
#o vetor C gerado.

n = int(input("quantos valores vai ter cada vetor: "))

veta : [int] = [0 for x in range(n)]
vetb : [int] = [0 for x in range(n)]
vetc : [int] = [0 for x in range(n)]

print("digite os valores do vetor A:")
for a in range(0, n):
    veta[a] = int(input())

print("digite os valores do vetor B:")
for i in range(0, n):
    vetb[i] = int(input())

print("Vetor Resultante: ")
for x in range(0,n):
    vetc[x] = veta[x] + vetb[x]
    print(vetc[x])

