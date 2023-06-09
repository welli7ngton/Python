# Dada uma lista de números, crie uma nova lista com os números que são primos 
# usando list comprehension.


def primo(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]


primos = [
    num 
    for num in numeros
    if primo(num)
]

print(primos)