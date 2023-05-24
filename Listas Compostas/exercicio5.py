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