n1 = int(input())
n2 = int(input())
n3 = int(input())
media = (n1 + n2 + n3) / 3

if media >= 7:
    print('Aprovado')
elif media < 7 and media >= 4:
    nf = int(input())
    if nf < 4:
        print('Reprovado')
    else:
        medf = (media + nf) / 2
        if medf >= 5:
            print('Aprovado')
        else:
            print('Reprovado')
else:
    print('Reprovado')
    