n = int(input("quantos numeros voce vai digitar? "))

for a in range(0,n):

    num = int(input("digite um numero: "))
    if num == 0:
        print("NULO")
    elif num %2 != 0 and num > 0:
        print("IMPAR POSITIVO")
    elif num %2 != 0 and num < 0:
        print("IMPAR NEGATIVO")
    elif num %2 == 0 and num > 0:
        print("PAR POSITIVO")
    else:
        print("PAR NEGATIVO")
