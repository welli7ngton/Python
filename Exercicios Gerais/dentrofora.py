n = int(input("quantos numeros voce vai digitar? "))
dentro = 0
fora = 0
for a in range(0, n):

    num = int(input("digite um numero: "))
    if num >= 10 and num <= 20:
        dentro += 1
    else:
        fora += 1

print(f"{dentro} =  Dentro")
print(f"{fora} = Fora")
