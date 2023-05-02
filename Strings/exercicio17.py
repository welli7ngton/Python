#Escreva um programa para converter uma cadeia de caracteres de letras maiusculas em ´
#letras minusculas


texto = input("digite um texto: ")
novaletra = 0
novotexto = ''

for a in range(len(texto)):

    if ord(texto[a]) > 64 and ord(texto[a]) < 91:
        novaletra = ord(texto[a]) + 32
        novotexto += chr(novaletra)
    else:
        novotexto += texto[a]    

print(novotexto)
