'''
Modifique seu código da atividade SOMA DE DUAS LISTAS implementando a função abaixo.

somar(L1, L2): Função que recebe duas listas de mesmo tamanho como parâmetro e cria uma terceira lista onde os elementos dessa terceira lista são a soma dos elementos das outras duas listas de cada índice. Depois retorna a terceira lista.

Use essa função no programa principal.

Entrada:

5

2 4 7 8 9

1 2 4 1 2

Saída:

3 6 11 9 11
'''

def somar(L1,L2):
    s = []
    for a in range(0, len(L1)):
        s.append(L1[a] + L2[a])
    
    return s

tam = int(input())

l1 = [0 for x in range(tam)]
l2 = [0 for x in range(tam)]

for a in range(0, tam):
    l1[a] = int(input())

for a in range(0, tam):
    l2[a] = int(input())

print(somar(l1,l2))