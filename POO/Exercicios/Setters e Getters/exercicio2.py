# 2- Crie uma classe chamada "Circle" com a propriedade radius. Implemente um setter para radius que verifica se o valor 
# passado é positivo.

class Circle:

    def __init__(self,radius):
        self.radius = radius

    
    def verifica_radius(self):
        if self.radius > 0:
            return True

        return False
    
c1 = Circle(0.120310301312031230203)
c2 = Circle(-1.120310301312031230203)

print(c1.verifica_radius())
print(c2.verifica_radius())
