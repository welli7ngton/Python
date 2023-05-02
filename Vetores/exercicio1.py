#Problema "negativos"
#Faça um programa que leia um número inteiro positivo N (máximo = 10) e depois N números inteiros
#e armazene-os em um vetor. Em seguida, mostrar na tela todos os números negativos lidos. 


n = int(input("digite um numero inteiro N com valor máximo de 10: "))

vet : [int] = [0 for x in range(n)]

for a in range(0,n):
    vet[a] = input("digite um número: ")

print("Numeros Negativos: ")
for i in range(0, n):
    if int(vet[i]) < 0:
        print(vet[i])
