from exercicio9 import racional


r1 = racional(2, 5)
r2 = racional(1, 4)
print("soma:")
numerador, denominador = r1.soma(r2)

print(numerador)
print("/")
print(denominador)

print(" ")

print("subtração:")
numerador, denominador = r1.sub(r2)

print(numerador)
print("/")
print(denominador)

print("produto:")
numerador, denominador = r1.produto(r2)

print(numerador)
print("/")
print(denominador)

print("divisao:")
numerador, denominador = r1.divisao(r2)

print(numerador)
print("/")
print(denominador)