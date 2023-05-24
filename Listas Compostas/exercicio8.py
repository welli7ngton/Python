'''
Você só pode fazer essa questão se fez a questão SOMA DE DUAS LISTAS (Função).

Implemente um programa que recebe duas listas de inteiros de mesmo tamanho e crie uma nova lista onde os elementos dessa nova lista é soma dos elementos das duas listas de entrada da seguinte forma: o primeiro elemento da primeira lista será somado com o último elemento da segunda lista, o segundo elemento da primeira lista será somado com o penúltimo elemento da segunda lista, e assim sucessivamente. Por exemplo,

suponha que as duas listas de entrada sejam L1 e L2 de tamanho 10 e S a lista resultante da soma. Então:

S[0] = L1[0] + L2[9]

S[1] = L1[1] + L2[8]

S[2] = L1[2] + L2[7]

...

S[9] = L1[9] + L2[0]

ATENÇÃO: OBRIGATORIAMENTE VC DEVE CRIAR AS TRÊS LISTAS, AS DUAS PRIMEIRAS PARA ARMAZENAR AS LISTAS DE ENTRADA E A TERCEIRA COM O RESULTADO, SÓ AÍ VC VAI IMPRIMIR.

Para isso, implemente a função somarV2(L1, L2) que cria e retorna uma lista com os elementos obtidos de acordo com a descrição acima. 

Entrada:

5

2 4 7 8 9

1 2 4 1 2

Saída:

4 5 11 10 10
'''
def somar(L1,L2):
    s = []
    t = len(L1) - 1
    for a in range(0, len(L1)):
        s.append(L1[a] + L2[t])
        t -= 1
        
    
    return s

tam = int(input())

l1 = [0 for x in range(tam)]
l2 = [0 for x in range(tam)]

for a in range(0, tam):
    l1[a] = int(input())

for a in range(0, tam):
    l2[a] = int(input())

print(somar(l1,l2,))