# Crie uma tupla com nomes de cinco países. Imprima os países em ordem
# alfabética.


t = ("brasil", "alemanha", "argentina", "holanda", "italia")

lista = [item.capitalize() for item in t]
lista = sorted(lista)
lista = tuple(lista)
print(lista)
