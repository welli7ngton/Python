#Problema "soma_vetor"
#Faça um programa que leia N números reais e armazene-os em um vetor. Em seguida:
# - Imprimir todos os elementos do vetor
# - Mostrar na tela a soma e a média dos elementos do vetor 

n = int(input("quantos numeros vai digitar : "))

vet : [float] = [0 for x in range(n)]

for a in range(0, n):
    vet[a] = float(input("digite um numero: "))

soma = sum(vet)

media = soma/n

print(f"Valores = {vet}")
print(f"Soma = {soma}")
print(f"Media = {media}")


