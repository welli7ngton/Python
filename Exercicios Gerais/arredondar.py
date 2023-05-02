import math
operacao = input()
nota = float(input())

if operacao == 'r':
    print(round(nota))
    #print(nota)
elif operacao == 'f':
    print(math.floor(nota))
    #print(nota)
elif operacao == 'c':
    print(math.ceil(nota))
    