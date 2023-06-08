# Escreva uma expressão lambda que retorne uma lista contendo apenas os números primos de 
# uma lista dada.


l = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19]

f = lambda x: list(
    filter(
        lambda y: all(
            y % num != 0 for num in range(2, int(y**0.5) + 1)
            )
            , x
        )
    )

print(f(l))
