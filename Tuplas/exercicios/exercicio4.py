# Crie uma função que receba duas tuplas como parâmetros e retorne uma nova
# tupla contendo os elementos comuns entre as duas tuplas.


def func(t1: tuple, t2: tuple):
    t3 = [n for n in t1 if n in t2]
    return tuple(t3)


t1 = (1, 2, 3, 4, 5, 6)
t2 = (1, 9, 7, 4, 9, 6)

t = func(t1, t2)
print(t)
