# 23-Escreva uma expressão lambda que converta todos os elementos de uma lista para letras maiúsculas.

# nova_lista = [expressão for elemento in sequência if condição]


l = ["q","w","e","r","t","y", "wellington"]

f = lambda lista: [
    lista[indice].upper() if lista[indice] == lista[indice].lower()
    else lista[indice]
    for indice in range(len(lista))
    ]

nova_lista = f(l)

print(nova_lista)