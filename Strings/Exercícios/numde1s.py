'''
Faça um programa que conte o numero de 1's que aparecem em um string. Exemplo: 
    0011001 -> 3

'''



num = input("digite o código: ")

qtd = 0

for a in range(0,len(num)):

    if num[a] == '1':
        qtd += 1
        

print(f"{num} -> {qtd}")


