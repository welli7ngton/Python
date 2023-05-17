'''
Faca um programa que receba do usuario uma string. O programa imprime a string sem 
suas vogais.
'''

nome = input("Digite uma string: ")
semvogal = ""

for letra in nome:
    if letra not in "aeiouAEIOU":
        semvogal += letra
    
print(semvogal)




    