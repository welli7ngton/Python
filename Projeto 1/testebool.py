sair = True

while sair == True:
    print("digite 1 para continuar e 2 para sair:")
    a = int(input())
    if a == 2:
        sair -= 1
    print()

print(bool(sair))
print(sair)