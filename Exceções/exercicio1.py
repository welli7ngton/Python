# Exercício de divisão segura:
# Escreva um programa que peça ao usuário para digitar dois números. Em seguida, divida o primeiro 
# número pelo segundo número, mas utilize try e except para lidar com a possibilidade de divisão 
# por zero. Caso ocorra uma divisão por zero, exiba uma mensagem adequada ao usuário.


while True:
    while True:
        try:
            n1 = int(input("Digite o primeiro número: "))
            break
        except ValueError:
            print("Erro de valor, digite um número e não uma letra")
            continue
    while True:
        try:
            n2 = int(input("Digite o segundo número: "))
            break
        except ValueError:
            print("Erro de valor, digite um número e não uma letra")
            continue

    while True:
        try:
            div = n1/n2
            break
        except ZeroDivisionError:
            print("Impossível dividir por 0.")
            continue
    print("O resultado da divisão foi:",div)
    print()
    print("Deseja continuar? (s/n)")
    while True:
        r = input()
        if r not in "snSN":
            print("digite 's' para continuar ou 'n' para encerrar.")
        else:
            break
    if r in "sS":
        break
    else:
        continue
