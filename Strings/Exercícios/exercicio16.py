#Leia uma cadeia de caracteres e converta todos os caracteres para maiuscula. Dica:
#subtraia 32 dos caracteres cujo codigo ASCII esta entre 65 e 90.


texto = input("Digite uma cadeia de caracteres: ")
novotexto = ''
codascii = 0

for a in range(len(texto)):

    if ord(texto[a]) > 96 and ord(texto[a]) < 123:

        codascii = ord(texto[a]) - 32
        novotexto += chr(codascii)
    else:
        novotexto += texto[a]

print(novotexto)






