# Crie uma função que receba uma tupla de números inteiros e retorne a média
# dos elementos.


def func(t: tuple) -> float:
    return sum(t)/len(t)


print(func((1, 2, 3, 4, 5, 6, 7, 8, 9, 0)))
