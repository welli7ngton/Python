# 10 -Crie uma classe chamada "Cachorro" com um método "latir" que imprime o som 
# "Au au!".

class Cachorro:

    def __init__(self,nome,idade):
        self.nome = nome.title()
        self.idade = idade
    
    def latir(self):
        print(self.nome, "está latindo!")
        print("\tAuAu!")
    
    def sentar(self):
        print(self.nome, "sentou.")

    def rolar(self):
        print(self.nome,"está rolando...")

    def pular(self):
        print(self.nome,"pulou!")

    def dar_a_pata(self):
        print(self.nome,"está dando a pata.")

c1 = Cachorro("Pulguento",1)

c1.latir()
c1.pular()
c1.rolar()
c1.sentar()
c1.dar_a_pata()

