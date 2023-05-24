'''
Implemente um programa que recebe duas listas de inteiros de tamanhos possivelmente diferentes e crie uma nova lista onde os elementos dessa nova lista serão a concatenação dos elementos da primeira lista com a segunda.

Vamos com um exemplo. A primeira lista tem tamanho 6: [8, 5, 7, 5, 16, 25]. A segunda lista tem tamanho 4: [78, 5, 25, 49]. A nova lista obtido pelo concatenação dos duas será: [8, 5, 7, 5, 16, 25, 78, 5, 25, 49].

Observe que todos os elementos da primeira lista foram adicionados na nova lista nas mesmas posições (índices). Já os elementos da segunda lita foram adicionados logo após o último elemento da primeira.

Você deve imprimir o tamanho desse vetor concatenação e na outra linha os seus elementos da lista resultante da concatenação.

ATENÇÃO: OBRIGATORIAMENTE VC DEVE CRIAR AS TRÊS LISTAS, AS DUAS PRIMEIRAS PARA ARMAZENAR AS LISTAS DE ENTRADA E A TERCEIRA COM O RESULTADO, SÓ AÍ VC VAI IMPRIMIR.

Entrada:
6                            #Tamanho da primeira lista
8 5 7 5 16 25
4                             #Tamanho da segunda lista
78 5 25 49
Saída:
10
8 5 7 5 16 25 78 5 25 49
'''


tam = int(input())
l1 = [0 for x in range(tam)]

for a in range(0, tam):
    l1[a] = int(input())
    
tam = int(input())
l2 = [0 for x in range(tam)]

for a in range(0, tam):
    l2[a] = int(input())

print(l1)
print(l2)


s = [0 for x in range(len(l1)+len(l2))]
for a in range(0, len(l1)):
    s[a] = l1[a]
pos = 0
for a in range(0,len(l2)):
    s[a + len(l1)] = l2[a]

print(len(s))
print(s)