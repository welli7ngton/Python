# 6- Crie uma classe chamada "Triângulo" com atributos de instância "lado1", "lado2" e "lado3" e um método 
# "verificar_tipo" que verifica se o triângulo é equilátero, isósceles ou escaleno

'''

Nesse caso, um triângulo pode ser escaleno, quando todos os lados possuem medidas diferentes; isósceles, quando existem dois lados que possuem mesma medida; ou equilátero, quando todos os lados são congruentes.

'''
class Triangulo:

    def __init__(self,lado1,lado2,lado3):
        self.lado1 = lado1
        self.lado2 = lado2
        self.lado3 = lado3
    
    def verifica_tipo(self):
        if self.lado1 != self.lado2 and self.lado1 != self.lado3 and self.lado1 != self.lado3:
            print("Escaleno.")
        elif self.lado1 == self.lado2 and self.lado2 == self.lado3:
            print("Equilátero.")
        elif self.lado1 == self.lado2 and self.lado3 != self.lado1 or self.lado2 == self.lado3 and self.lado1 != self.lado2:
            print("Isósceles.")

t1=Triangulo(1,2,3)
t2=Triangulo(3,2,3)
t3=Triangulo(3,3,3)

t1.verifica_tipo()
t2.verifica_tipo()
t3.verifica_tipo()