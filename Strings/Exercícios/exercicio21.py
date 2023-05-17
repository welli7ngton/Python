#Faca um programa que preencha um vetor com os modelos de cinco carros (exemplos de
#modelos: Fusca, Gol, Vectra, etc.). Preencha outro vetor com o consumo desses carros,
#isto e, quantos quilometros cada um deles faz com um litro de combustıvel. Calcule e
#mostre:
#   (a) O modelo de carro mais economico; 
#   (b) Quantos litros de combustıvel cada um dos carros cadastrados consomem para
#       percorrer uma distancia de 1.000 quilometros.

vmodelos = [0 for x in range(5)]

vconsumo = [0 for x in range(5)]

vlitros = [0 for x in range(5)]

menorconsumo = 10000.0
economico = ''
for a in range(0,5):
    vmodelos[a] = input("digite o modelo do carro: ")
    vconsumo[a] = float(input("digite o consumo do carro em km/l: "))
    print()

    if vconsumo[a] < menorconsumo:
        menorconsumo = vconsumo[a]
        economico = vmodelo[a]

    vlitros[a] = 1000/vconsumo[a]

print(f"o carro com menor consumo é: {economico}, com consumo de {menorconsumo}")
print()
for a in range(0, 5):
    print(f"o consumo em litros de cada carro respectivamente é: {vlitros[a]}")