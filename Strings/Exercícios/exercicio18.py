#Leia um vetor contendo letras de uma frase inclusive os espac¸os em branco. Retirar os
#espac¸os em branco do vetor e depois escrever o vetor resultante.

frase = input("digite uma frase: ")
novafrase = ''
for caractere in frase:

    if caractere != ' ':
        novafrase += caractere

print(novafrase)

    




