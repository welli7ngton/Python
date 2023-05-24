'''Implemente um programa que recebe duas listas de inteiros de mesmo tamanho e crie uma nova lista onde os elementos dessa nova lista é soma dos elementos das duas listas, posição a posição. Ou seja, o primeiro elemento dessa nova lista será a soma dos primeiros elementos das duas listas de entrada. O segundo elemento será a soma dos segundos elementos das duas listas. E assim sucessivamente.

suponha que as duas listas de entrada sejam L1 e L2 de tamanho 10 e S a lista resultante da soma. Então:

S[0] = L1[0] + L2[0]

S[1] = L1[1] + L2[1]

S[2] = L1[2] + L2[2]

...

S[9] = L1[9] + L2[9]

ATENÇÃO: OBRIGATORIAMENTE VC DEVE CRIAR AS TRÊS LISTAS, AS DUAS PRIMEIRAS PARA ARMAZENAR AS LISTAS DE ENTRADA E A TERCEIRA COM O RESULTADO, SÓ AÍ VC VAI IMPRIMIR.

Entrada:

5

2 4 7 8 9

1 2 4 1 2

Saída:

3 6 11 9 11
'''

tam = int(input())

l1 = [0 for x in range(tam)]
l2 = [0 for x in range(tam)]

for a in range(0, len(l1)):
    l1[a] = int(input())

for a in range(0, len(l2)):
    l2[a] = int(input())

s = []

for a in range(0, len(l1)):
    s.append(l1[a] + l2[a])

print(s)