num1 = int(input())

if num1 % 2 == 0:
    num2 = int(input())
    num3 = int(input())
    if num2 % 2 == 0:
        if num3 % 2 == 0:
            soma = num2 + num3
            print('{} é um número par e a soma dos números pares dar {}'.format(num1, soma))
        elif num2 % 2 != 0:
            if num3 % 2 == 0:
                soma = num3
                print('{} é um número par e a soma dos números pares dar {}'.format(num1, soma))
        elif num2 % 2 == 0:
            if num3 % 2 != 0:
                soma = num2
                print('{} é um número par e a soma dos números pares dar {}'.format(num1, soma))
    elif num2 % 2 != 0:
        if num3 % 2 != 0:
            soma = 0
            print('{} é um número par e a soma dos números pares dar {}'.format(num1, soma))

elif num1 % 2 != 0:
    num2 = int(input())
    num3 = int(input())
    num4 = int(input())
    if num2 % 2 != 0:
        if num3 % 2 != 0:
            if num4 % 2 != 0:
                soma = num2 + num3 + num4
                print('{} é um número impar e a soma dos números impares dar {}'.format(num1, soma))
    elif num2 % 2 == 0:
        if num3 % 2 != 0:
            if num4 % 2 != 0:
                soma = num3 + num4
                print('{} é um número impar e a soma dos números impares dar {}'.format(num1, soma))
    elif num2 % 2 != 0:
        if num3 % 2 == 0:
            if num4 % 2 == 0:
                soma = num2
                print('{} é um número impar e a soma dos números impares dar {}'.format(num1, soma))
    elif num2 % 2 == 0:
        if num3 % 2 == 0:
            if num4 % 2 != 0:
                soma = num4
                print('{} é um número impar e a soma dos números impares dar {}'.format(num1, soma))

    elif num2 % 2 == 0:
        if num3 % 2 == 0:
            if num4 % 2 == 0:
                soma = 0
                print('{} é um número impar e a soma dos números impares dar {}'.format(num1, soma))