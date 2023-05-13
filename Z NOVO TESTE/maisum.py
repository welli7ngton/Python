#Problema "maior_posicao"
#Faça um programa que leia N números reais e armazene-os em um vetor. Em seguida, mostrar na tela
#o maior número do vetor (supor não haver empates). Mostrar também a posição do maior elemento,
#considerando a primeira posição como 0 (zero). 


n = int(input("quantos numeros vai digitar? "))

vet : [float] = [0 for x in range(n)]

maiornumero = 0
pos = 0
for a in range(0, n):

    vet[a] = float(input("digite o numero: "))
    if vet[a] > maiornumero:
        maiornumero = vet[a]
        pos = vet.index(maiornumero)


print(f"maior valor: {maiornumero}")
print(f"posição do maior valor: {pos}")


# listaDeNomes = ['Fulano', 'Fulana', 'DeTal', 'Ihechikara']

# print(listaDeNomes.index('Fulana'))
# 1