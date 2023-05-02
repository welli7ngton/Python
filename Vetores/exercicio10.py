#Problema "aprovados"
#Fazer um programa para ler um conjunto de N nomes de alunos, bem como as notas que eles tiraram
#no 1º e 2º semestres. Cada uma dessas informações deve ser armazenada em um vetor. Depois, imprimir
#os nomes dos alunos aprovados, considerando aprovados aqueles cuja média das notas seja maior ou
#igual a 6.0 (seis). 


n = int(input("digite a quantidade de alunos: "))

nomes : [str] = [0 for x in range(n)]
sem1 : [float] = [0 for x in range(n)]
sem2 : [float] = [0 for x in range(n)]
media : [float] = [0 for x in range(n)]

for a in range(0,n):
    print(f"digite o nome, primeira e segunda nota do {a + 1}o aluno: ")
    nomes[a] = input()
    sem1[a] = float(input())
    sem2[a] = float(input())
    media[a] = (sem1[a] + sem2[a])/2

print("Aprovados: ")
for b in range(0,len(media)):
    if media[b] >= 6.0:
        print(nomes[b])