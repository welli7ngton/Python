# 2- Crie uma classe chamada "Retângulo" com atributos de instância "largura" e "altura" e um método "calcular_area" 
# que retorna a área do retângulo.


class Retangulo:

    def __init__(self,largura,altura):
        self.largura = largura
        self.altura = altura
    
    def calcular_area(self):
        area = self.largura * self.altura
        return area
    

r1 = Retangulo(4,4)
print(r1.calcular_area())

r2 = Retangulo(3,8)
print(r2.calcular_area())

r3 = Retangulo(9,23)
print(r3.calcular_area())