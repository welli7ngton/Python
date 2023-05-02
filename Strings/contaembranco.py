'''

Ler uma frase e contar quantos caracteres sao brancos. Lembre-se que uma frase  e um 
conjunto de caracteres (vetor).

'''



frase = input("digite uma frase: ")

qtdbranco = 0

for branco in frase:
    if branco == ' ':
        qtdbranco += 1
        
print(qtdbranco)