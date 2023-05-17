#Faca um programa que receba duas frases distintas e imprima de maneira invertida,
#trocando as letras A por *

frase1 = input("digite uma frase: ")
frase2 = input("digite outra frase: ")
frases = frase1 + ' ' + frase2
novafrase = ''

for letra in frases:
    if letra not in 'aA':
        novafrase += letra
        
    else:
        novafrase += '*'
        

print(novafrase[::-1])
