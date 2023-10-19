casos = int(input("quantos casos voce vai digitar? "))

div = 0

for a in range(0, casos):

    num = int(input("numerador: "))
    den = int(input("denominador: "))

    if den == 0:
        print("divisão impossivel")
    else:
        div = num / den
        print(f"divisão = {div}")
