# Faça um programa que recebe três números do usuário, e identifica o maior
# através de uma função e o menor número através de outra função.Achar maior
# e menor número com funções


def higher(n1: int | float, n2: int | float, n3: int | float) -> int | float:
    return max(n1, n2, n3)


def lower(n1: int | float, n2: int | float, n3: int | float) -> int | float:
    return min(n1, n2, n3)


if __name__ == '__main__':
    print(higher(1, 2, 3))
    print(lower(1, 2, 3))
