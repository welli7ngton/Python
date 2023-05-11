#7. Crie uma classe que modele um carro
#(a) Atributos: marca, ano e preco
#(b) Metodos: mostrar preco e de exibicao dos dados
#Leia os dados de 5 carros e um valor p, Mostre as informacoes de todos os carros com 
#preco menor que p.


class Carro:
    
    def __init__(self, marca, ano, preco):
        self.marca = marca
        self.ano = ano
        self.preco = preco

    def mostra_preco(self):
        print(f"Preço: R${self.preco:.2f}")

    def dados(self):
        print(f"Marca: {self.marca}")
        print(f"Ano: {self.ano}")
        self.mostra_preco()
        print("")

