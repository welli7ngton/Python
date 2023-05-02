num = int(input("digite um numero inteiro: "))

soma = num
cont = 4


if num %2 == 0:
    while cont != 0:
        num += 2
        soma += num
        cont -= 1   
else:
    numpar = num + 1
    soma = numpar
    while cont != 0:
        
        numpar += 2
        soma += numpar
        cont -= 1    

print(f"soma = {soma}")