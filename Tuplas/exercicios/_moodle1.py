# Implemente um programa que recebe uma lista de inteiros e seu programa deve
# imprimir a quantidade de números pares, impares e nulos da lista.

# Para isso, implemente uma função que recebe uma lista como parâmetros e
# retorna via tupla a quantidade de números pares, impares e nulos da lista.

# Entrada:

# 2 5 8 2 6 4 2 0 0
# Saída:
# A lista contem 6 pares, 1 impares e 2 zeros

# Entrada:
# 11 70 4 9 70 14 70
# Saída:
# A lista contem 4 pares, 2 impares e 0 zeros


def funcao(lista):
    pares = impares = nulos = 0
    for i in lista:
        if i == 0:
            nulos += 1
            continue
        if i % 2 == 0:
            pares += 1
        else:
            impares += 1

    return f"A lista contem {pares} pares, {impares} impares e {nulos} zeros"


s = funcao([11, 70, 4, 9, 70, 14, 70])
print(s)
