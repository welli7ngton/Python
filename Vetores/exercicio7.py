#Problema "abaixo_da_media"
#Fazer um programa para ler um número inteiro N e depois um vetor de N números reais. Em seguida,
#mostrar na tela a média aritmética de todos elementos com três casas decimais. Depois mostrar todos
#os elementos do vetor que estejam abaixo da média, com uma casa decimal cada. 


n = int(input("quantos elementos vai ter o vetor? "))

vet : [float] = [0 for x in range(n)]
media = 0
abaixo_da_media = []
for a in range(0,n):
    vet[a] = float(input("digite um numero: "))
    

media = sum(vet) /n

for i in range(0,n):
    if vet[i] < media:
        abaixo_da_media.append(vet[i])

print(f"média do vetor: {media:.3f}")
print("Elementos abaixo da média: ")
for b in range(0,len(abaixo_da_media)):
    print(abaixo_da_media[b])