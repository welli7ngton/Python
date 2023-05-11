#Implemente uma classe para representar em vetor (x,y,z) no R3 Implemente os metodos para calcular a soma, 
#subtracao, produto vetorial, produto escalar e modulo.


class Vetor:

    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    def soma(self, x1, y2, z3):
        somax = self.x + x1
        somay = self.y + y2
        somaz = self.z + z3

        print(f"a soma dos vetores é: ")
        print(f"x = {somax}")
        print(f"y = {somay}")
        print(f"z = {somaz}")

    def sub(self, x1, y2, z3):
        subx = self.x - x1
        suby = self.y - y2
        subz = self.z - z3

        print(f"a subtração dos vetores é: ")
        print(f"x = {subx}")
        print(f"y = {suby}")
        print(f"z = {subz}")
    
    def prod_vetorial(self, x1, y2, z3):
        x = (self.y * z3) - (self.z * y2)
        y = (self.z * x1) - (self.x * z3)
        z = (self.x * y2) - (self.y * x1)

        print(f"produto vetorial: ({x}, {y}, {z})")

    def prod_escalar(self, x1, y2, z3):
        p = (self.x * x1) + (self.y * y2) + (self.z * z3)

        print(f"produto escalar: {p}")
    
    def modulo(self):
        mod = self.x**2 + self.y**2 + self.z**2

        print(f"Módulo do vetor: {mod}")