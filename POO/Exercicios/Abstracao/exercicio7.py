# Crie uma classe abstrata chamada InstrumentoMusical com métodos abstratos tocar() e afinar(). Implemente classes 
# concretas para representar diferentes instrumentos musicais, como piano, violão e bateria. Cada classe deve fornecer 
# uma implementação adequada dos métodos abstratos.

class InstrumentoMusical:

    def tocar(self,musica):
        pass

    def afinar(self):
        pass



class Violao(InstrumentoMusical):

    def __init__(self):
        print(f"{__class__.__name__} está pronto para tocar!")
        self.afinacao = 100

    def tocar(self,musica):
        if self.afinacao < 5:
            print("O violão está desafinado e não pode tocar, afine o violão para tocar a musica desejada.")
            return False
        print(f"{__class__.__name__} está tocando {musica}...")
        self.afinacao -= 15
    
    def afinar(self):
        if self.afinacao == 100:
            print("O violão já está afinado.")
            return False
        print("O violão está sendo afinado...")
        self.afinacao = 100
        return True

class Bateria(InstrumentoMusical):

    def __init__(self):
        print(f"{__class__.__name__} está pronta para tocar!")
        self.estado_baquetas = 100

    def tocar(self,musica):
        if self.estado_baquetas < 5:
            print("As baquetas estão muito danificadas, arrume elas para poder tocar a musica.")
            return False
        print(f"{__class__.__name__} está tocando {musica}...")
        self.estado_baquetas -= 15
    
    def afinar(self):
        if self.estado_baquetas == 100:
            print("As baquetas já estão funcionando.")
            return False
        print("As baquetas estão sendo consertadas...")
        self.estado_baquetas = 100
        return True
    

v1 = Violao()
b1 = Bateria()
v1.afinar()
v1.tocar("Everybody wants to rule the world")
v1.tocar("Everybody wants to rule the world")
b1.tocar("Everybody wants to rule the world")
b1.tocar("Everybody wants to rule the world")
b1.tocar("Everybody wants to rule the world")
b1.tocar("Everybody wants to rule the world")
b1.tocar("Everybody wants to rule the world")
b1.tocar("Everybody wants to rule the world")
v1.tocar("Everybody wants to rule the world")
b1.tocar("Everybody wants to rule the world")
v1.tocar("Everybody wants to rule the world")
v1.tocar("Everybody wants to rule the world")
v1.tocar("Everybody wants to rule the world")
v1.tocar("Everybody wants to rule the world")
v1.tocar("Everybody wants to rule the world")
b1.tocar("Everybody wants to rule the world")
v1.afinar()
b1.afinar()
v1.tocar("Everybody wants to rule the world")
b1.tocar("Everybody wants to rule the world")