# 5- Crie uma classe chamada "Carro" com atributos de instância "marca" e "modelo" e um método "apresentar_carro" 
# que imprime a marca e o modelo do carro.



class Carro:

    def __init__(self,marca,modelo,ano,cor,km_rodados):
        self.marca = marca
        self.modelo = modelo
        self.ano = ano
        self.cor = cor
        self.km_rodados = km_rodados

    def apresentar_carro(self):
        print(f"Marca: {self.marca}")
        print(f"Modelo: {self.modelo}")
        print(f"ano: {self.ano}")
        print(f"cor: {self.cor}")
        print(f"Quilômetros Rodados: {self.km_rodados}km")

c1 = Carro("Fiat","Uno",2009,"Branco",10000)
c2 = Carro("Renaut","Kwid",2015,"Preto",7000)
c3 = Carro("Toyota","Corola",2018,"Prata",0)
c1.apresentar_carro()
c2.apresentar_carro()
c3.apresentar_carro()