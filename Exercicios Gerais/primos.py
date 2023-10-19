num = int(input("digite um numero: "))
primo = 0
for a in range(0, num + 1):
    if num % (a + 1) == 0:
        primo += 1

if primo > 2:
    print(f"{num} não é primo")
else:
    print(f"{num} é primo")
