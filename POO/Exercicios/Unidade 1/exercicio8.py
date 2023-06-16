# 8- Crie uma classe chamada "Animal" com um método "emitir_som" que imprime 
# o som que o animal faz.


class Animal:

    def __init__(self, nome,som):
        self.nome = nome
        self.som = som
    
    def emitir_som(self):
        print(self.som)


gato = Animal("Gato","Miau")

cachorro = Animal("Cachorro","AuAu")

vaca = Animal("Vaca","Muuu")

gato.emitir_som()
vaca.emitir_som()
cachorro.emitir_som()