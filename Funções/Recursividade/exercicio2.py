# Defina a função div que recebe como argumentos dois números naturais  m
# e  n  e devolve o resultado da divisão inteira de  m por  n
# Neste exercício não pode recorrer às operações aritméticas de multiplicação, divisão e resto da divisão inteira


def div(m,n):
    if m < n:
        return 0
    else:
         
        return 1 + div(m - n, n)
    

a =  div(6,2)

print(a)