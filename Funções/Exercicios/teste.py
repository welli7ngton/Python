lista = input().split(",")
lista = list(lista)

r = list()

for a in range(len(lista),0,-1):
    r.append(lista[a-1])

a = lista == r 

print(a)
