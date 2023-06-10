# Exercício de manipulação de lista:
# Escreva um programa que declare uma lista vazia. Em seguida, peça ao usuário para digitar um 
# número. Utilize try e except para tratar a possibilidade de o usuário digitar um valor inválido, 
# como uma string. Caso ocorra um erro na conversão, exiba uma mensagem adequada ao usuário. Caso o 
# valor seja válido, adicione-o à lista e exiba a lista atualizada. Repita esse processo até que o 
# usuário digite a palavra "fim".


lista = []

while True:
    print("Digite um número:")
    try:
        n = input()
        n = int(n)
        lista.append(n)
        print(lista)
    except ValueError:
        if n == "fim":
            break
        else:
            print("Você não digitou um número, para encerrar digite 'fim'.")
