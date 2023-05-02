#Implemente um programa que leia duas strings, str1 e str2, e um valor inteiro positivo
#N. Concatene nao mais que N caracteres da string  str2 a string  str1 e termine str1 com
#NULL.



str1 = input("digite a primeira string: ")
str2 = input("digite a segunda string: ")

n = int(input("digite o concatenador: "))

if n <= len(str2):


    novastr2 = ""

    for a in range(0, n ):

        novastr2 += str2[a]

    for a in range(0, len(novastr2)):

        str1 += novastr2[a]



    str1 += "NULL"
    print(str1)
else:
    print(f"o N inserido é maior que o tamanho da palavra {str2}. O programa não poderá ser executado.")