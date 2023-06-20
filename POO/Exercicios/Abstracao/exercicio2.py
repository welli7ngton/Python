# Crie uma classe abstrata chamada Animal com métodos abstratos emitir_som() e mover(). Implemente classes concretas 
# para representar diferentes animais, como cão, gato e pássaro. Cada classe deve fornecer uma implementação adequada 
# dos métodos abstratos.


class Animal:

    def emitir_som(self,som):
        pass

    def acao(self,acao):
        pass

class Cao(Animal):
    def __init__(self,nome):
        self.nome = nome

    def emitir_som(self,som):
        print("Nome:",self.nome)
        print("Som:",som)

    def acao(self,acao):
        print("Ação:",acao)


class Gato(Animal):
    def __init__(self,nome):
        self.nome = nome

    def emitir_som(self,som):
        print("Nome:",self.nome)
        print("Som:",som)

    def acao(self,acao):
        print("Ação:",acao)


class Passaro(Animal):
    def __init__(self,nome):
        self.nome = nome

    def emitir_som(self,som):
        print("Nome:",self.nome)
        print("Som:",som)

    def acao(self,acao):
        print("Ação:",acao)

cachorro = Cao("Pulguento")
cachorro.emitir_som("AuAu")
cachorro.acao("Pulando")
gato = Gato("Xande")
gato.emitir_som("Miau")
gato.acao("Corendo")
passaro = Passaro("Galo")
passaro.emitir_som("Cócóricó")
passaro.acao("Dormindo")