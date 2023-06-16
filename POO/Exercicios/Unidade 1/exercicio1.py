# 1- Crie uma classe chamada "Círculo" com um atributo de instância "raio" e um método "calcular_area" que retorna a 
# área do círculo.


class Circulo:

    def __init__(self,raio):
        self.raio = raio
    
    def calcular_area(self):
        area = 3.1415*(self.raio**2)
        return area

c1 = Circulo(5)
print(f"{c1.calcular_area():.4f}")
c2 = Circulo(7)
print(f"{c2.calcular_area():.4f}")
c3 = Circulo(25)
print(f"{c3.calcular_area():.4f}")
c4 = Circulo(2)
print(f"{c4.calcular_area():.4f}")

