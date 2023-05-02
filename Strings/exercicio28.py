#Faca um programa que, dada uma string, diga se ela e um palındromo ou nao. Lem- 
#brando que um palındromo e uma palavra que tenha a propriedade de poder ser lida 
#tanto da direita para a esquerda como da esquerda para a direita. Exemplo:
#ovo
#arara
#SocorrammesubinoonibusemMarrocos.
#Anotaramadatadamaratona



frase = input("digite a frase: ")
frase = frase.lower()


frase2 = ""

frase2 = frase[::-1]

if frase2 == frase:
    print("é um palindromo.")
else:
    print("não é um palindromo.")