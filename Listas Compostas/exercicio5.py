'''
Implemente um programa que receba duas listas de inteiros de mesmo tamanho e depois, o valor de um índice válido dessas listas. Troque os elementos do índice informado dessas duas listas. Depois imprima listas modificadas. 

ATENÇÃO: Você somente pode imprimir depois de fazer as modificações no vetor.

A entrada terá a seguinte ordem: A primeira informação será a quantidade de números das listas, depois os elementos da primeira lista. Depois os elementos da segunda lista. Por fim, o índice para a realização da troca.

Entrada:

2       
8 5    
1 10
0       

Saída:
1 5
8 10

Entrada:
8
2 8 8 8 8 4 4 6
10 10 9 2 9 3 7 7
6

Saída:
2 8 8 8 8 4 7 6
10 10 9 2 9 3 4 7
'''

l1 = []
l2 = []

tam = int(input())
a = 0
while a < tam:
    l1.append(input())
    a += 1
a = 0
while a < tam:
    l2.append(input())
    a += 1
    
indice = int(input())

l1[indice], l2[indice] = l2[indice], l1[indice]

print(l1)
print(l2)