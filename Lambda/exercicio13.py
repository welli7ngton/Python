# Escreva uma expressão lambda que verifique se um número é primo.

def executa(fun,n):
    return fun(n)
l = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97]
# l = [i for i in range(101)]

for i in range(len(l)):
    print(l[i]," = ",executa(lambda x:True if x == 2 or x == 3 or x %2 != 0 and x%3 != 0   else False, l[i]))

f = lambda x: True if x == 2 or x == 3 or x %2 != 0 or x%3 != 0   else False

for a in range(len(l)):
    print()