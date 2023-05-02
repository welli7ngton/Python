frase = input("digite uma frase: ")
frase2 = str
total = len(frase) - 1


for a in range(len(frase), 0, -1):
    frase[total] = frase[total]
    total -= 1



if frase2 == frase:
    print("é um palndromo: ")
    print()
    print(frase)
    print()
    print(frase2)
else:
    print("não é um palindromo: ")
    print()
    print(frase)
    print()
    print(frase2)

      #      if naipe == 'C':
      #      vetc[posvetc] = (1)
      #      posvetc = posvetc + 1