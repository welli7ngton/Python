# Crie uma classe abstrata chamada Veiculo com métodos abstratos acelerar() e frear(). Implemente classes concretas 
# para representar diferentes tipos de veículos, como carro, moto e bicicleta. Cada classe deve fornecer uma 
# implementação adequada dos métodos abstratos.
import time
class Veiculo:

    def acelerar(self):
        ...

    def frear(self):
        ...


class Carro(Veiculo):
    
    def __init__(self,vel_acele):
        self.vel_acele = vel_acele
        self.vel_atual = 0

    def acelerar(self):
        self.vel_atual += self.vel_acele
        print(f"{__class__.__name__} está acelerando...")
        print(f"Velocidade atual: {self.vel_atual}km/h")
        time.sleep(1)
    
    def frear(self):
        print(f"{__class__.__name__} está freando...")
        while self.vel_atual > 0:
            time.sleep(1)
            print(self.vel_atual,"km/h")
            self.vel_atual -= 10
        print(self.vel_atual,"km/h")
        print("O carro parou.")

class Moto(Veiculo):

    def __init__(self,vel_acele):
        self.vel_acele = vel_acele
        self.vel_atual = 0

    def acelerar(self):
        self.vel_atual += self.vel_acele
        print(f"{__class__.__name__} está acelerando...")
        print(f"Velocidade atual: {self.vel_atual}km/h")
        time.sleep(1)

    def frear(self):
        print(f"{__class__.__name__} está freando...")
        while self.vel_atual > 0:
            print(self.vel_atual,"km/h")
            self.vel_atual -= 10
            time.sleep(1)
        print(self.vel_atual,"km/h")
        print("A moto parou.")


c1 = Carro(30)
c1.acelerar()
c1.acelerar()
c1.acelerar()
c1.frear()

m1 = Moto(20)
m1.acelerar()
m1.acelerar()
m1.acelerar()
m1.frear()
