'''
Faca um programa que receba uma palavra e calcule quantas vogais (a, e, i, o, u) possui
essa palavra. Entre com um caractere (vogal ou consoante) e substitua todas as vogais
da palavra dada por esse caractere.
'''

palavra = input("Digite uma palavra: ")

# Contagem de vogais
vogais = 0
for letra in palavra:
    if letra in "aeiouAEIOU":
        vogais += 1

print(f"A palavra {palavra} possui {vogais} vogais.")

# Substituição de vogais
caractere = input("Digite um caractere (vogal ou consoante): ")
nova_palavra = ""
for letra in palavra:
    if letra in "aeiouAEIOU":
        nova_palavra += caractere
    else:
        nova_palavra += letra

print(f"A nova palavra é: {nova_palavra}")
        
        




      
     
