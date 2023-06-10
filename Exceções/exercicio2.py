# Exercício de conversão de string para inteiro:
# Escreva um programa que peça ao usuário para digitar um número como string. Em seguida, tente 
# converter essa string para um número inteiro utilizando a função int(). Utilize try e except para 
# tratar a possibilidade de o usuário digitar uma string que não possa ser convertida para um 
# número inteiro. Caso ocorra um erro na conversão, exiba uma mensagem adequada ao usuário.


while True:
    print("Digite uma sequencia que possa ser convertida para inteiro.")
    num = input()
    try:
        num = int(num)
    except ValueError:
        print("A sequência não pode ser convertida para um número inteiro.")
        letras = []
        for i in num:
            if i.isdigit() == False:
                letras.append(i)
        print("Caracteres que não podem ser convertidos:",letras)
        print()
        continue
    else:
        print("A sequência foi convertida para inteiro.")
        break