# Crie uma classe abstrata chamada Forma com um método abstrato calcular_area(). Implemente classes concretas para 
# representar diferentes formas geométricas, como quadrado, retângulo e círculo. Cada classe deve fornecer uma 
# implementação adequada do método calcular_area().

# super class | classe abstrata
class Forma:
    def calcular_area(self,*args):
        pass

# sub classes | classes herdeiras da abstração
class Quadrado(Forma):
    def calcular_area(self,*args):
        base, altura = args
        return f"Área do Quadrado: {base*altura}"

class Triangulo(Forma):
    def calcular_area(self,*args):
        base, altura = args
        return f"Área do Triângulo: {(base*altura)/2}"
        
class Trapezio(Forma):
    def calcular_area(self,*args):
        base_maior, base_menor,altura= args
        return f"Área do Trapézio: {((base_maior*base_menor)*altura)/2}"

class Cilindro(Forma):
    def calcular_area(self,*args):
        raio, altura = args
        return f"Área do Trapézio: {(2*3.1415)*raio*altura}"

class Cone(Forma):
    def calcular_area(self,*args):
        raio, g = args
        return f"Área do Trapézio: {3.1415*(raio*(raio + g))}"
        

q = Quadrado()
print(q.calcular_area(5,5))
t = Triangulo()
print(t.calcular_area(5,3))
trap = Trapezio()
print(trap.calcular_area(5,3,4))
cilindro = Cilindro()
print(cilindro.calcular_area(5,2))
cone = Cone()
print(cone.calcular_area(5,3))
