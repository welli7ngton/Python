soma = 0

for a in range(0, 6):
    num = int(input("digite um numero: "))
    if num % 2 == 0:
        soma += num

print(f"a soma dos numeros pares é: {soma}")
