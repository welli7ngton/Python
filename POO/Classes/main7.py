from exercicio7 import Carro


carros = []
p = float(input("Digite o valor máximo para o preço: "))

for i in range(3):
    marca = input("Digite a marca do carro: ")
    ano = int(input("Digite o ano do carro: "))
    preco = float(input("Digite o preço do carro: "))
    carro = Carro(marca, ano, preco)
    carros.append(carro)

print(f"Carros com preço menor que R${p}:")
for carro in carros:
    if carro.preco < p:
        carro.dados()

