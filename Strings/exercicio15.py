'''
Faca um programa que leia uma palavra e some 1 no valor ASCII de cada caractere da
palavra. Imprima a string resultante.

'''

palavra = input("Digite uma palavra: ")
nova_palavra = ""
for letra in palavra:
    novo_valor_ascii = ord(letra) + 1
    nova_letra = chr(novo_valor_ascii)
    nova_palavra += nova_letra

print("Palavra com valor ASCII aumentado em 1: ", nova_palavra)


