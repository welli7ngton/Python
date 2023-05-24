'''Implemente um programa que receba duas listas de inteiros de mesmo tamanho e troque os elementos entre as duas listas de índices pares, depois imprima os vetores modificados. 

ATENÇÃO: Você somente pode imprimir as listas depois de fazer as modificações.

OBS: Considere o índice 0 como sendo par.

A entrada terá a seguinte ordem: A primeira informação será a quantidade de números das listas, depois os elementos da primeira lista. Depois os elementos da segunda lista.

Entrada:
4
1 2 3 4
7 8 9 10

Saída
7 2 9 4
1 8 3 10

Entrada:
6
8 4 9 5 6 1
1 3 7 2 4 8

Saída
1 4 7 5 4 1
8 3 9 2 6 8'''

tam = int(input())

l1 = [0 for x in range(tam)]
l2 = [0 for x in range(tam)]

for a in range(0,len(l1)):
    l1[a] = int(input())

for a in range(0,len(l2)):
    l2[a] = int(input())

for a in range(0, len(l1)):
    if a %2 == 0:
        l1[a], l2[a] = l2[a], l1[a]
        
print(l1)
print(l2)