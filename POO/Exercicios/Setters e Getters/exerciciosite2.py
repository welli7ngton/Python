# Crie uma classe chamada Ponto3D. Essa classe deve possuir 3 atributos privados do tipo inteiro: px,py e pz. Além 
# disso, essa classe deve possuir 2 métodos públicos. O primeiro,setponto , deve receber 3 argumentos e passar esses 
# valores para os 3 atributos da classe. O segundo,printponto , deve imprimir esses valores no padrão px,py,pz.


class Ponto3D:

    def __init__(self):
        self.px = None
        self.py = None
        self.pz = None

    # getter
    @property
    def get_valores(self):
        return self.px,self.py,self.pz

    # setter
    @get_valores.setter
    def get_valores(self,args):
        self.px = args[0]
        self.py = args[1]
        self.pz = args[2]
    
    def print_ponto(self):
        print(f"px = {self.px}, py = {self.py}, pz = {self.pz}")


p1 = Ponto3D()

p1.get_valores = 1,2,3

p1.print_ponto()