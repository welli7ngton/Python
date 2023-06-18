# Exercício com classes
# 1 - Crie uma classe Carro (Nome)
# 2 - Crie uma classe Motor (Nome)
# 3 - Crie uma classe Fabricante (Nome)
# 4 - Faça a ligação entre Carro tem um Motor
# Obs.: Um motor pode ser de vários carros
# 5 - Faça a ligação entre Carro e um Fabricante
# Obs.: Um fabricante pode fabricar vários carros
# Exiba o nome do carro, motor e fabricante na tela


class Carro:
    def __init__(self,nome,ano):
        self.nome = nome
        self.ano = ano
        self.motor = None
        self.fabricante = None

    def add_motor(self,nome_motor):
        motor = Motor(nome_motor)
        self.motor = motor.nome
    
    def add_fabricante(self,nome_fabricante):
        fabricante = Fabricante(nome_fabricante)
        self.fabricante = fabricante.nome

class Motor:
    def __init__(self,nome):
        self.nome = nome

class Fabricante:
    def __init__(self,nome):
        self.nome = nome


fusca = Carro("Fusca",2003)

fusca.add_fabricante("Volkswagen")
fusca.add_motor("1.0")

uno = Carro("Uno Mille",2010)
uno.add_fabricante("Fiat")
uno.add_motor("1.0")

corolla = Carro("Corolla",2010)
corolla.add_fabricante("Toyota")
corolla.add_motor("2.0")


print("Dados:",fusca.nome,fusca.ano,fusca.motor,fusca.fabricante)
print()
print("Dados:",uno.nome,uno.ano,uno.motor,uno.fabricante)
print()
print("Dados:",corolla.nome,corolla.ano,corolla.motor,corolla.fabricante)
print()
