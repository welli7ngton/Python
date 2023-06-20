# Tamagotchi
# Você deve implementar um simulador de bichinho virtual. Ele poderá comer, brincar, dormir e tomar banho. E eventualmente morrerá, se você não cuidar bem dele.

# Intro
# Seu sistema deverá:

# Inicializar
# passando energia, saciedade e limpeza máximas do pet.
# Todos os níveis devem ser iniciados no máximo na criação do pet.
# Os outros atributos são
# diamantes, que ele vai ganhar jogando.
# e idade que aumenta a cada ação realizada,
# ambos iniciando em 0.
# Comendo, Jogando, Dormindo e tomando banho
# Cada operação causa aumento e reduções nos atributos.
# Nenhum atributo pode passar do máximo ou ir abaixo de 0.
# Morrendo
# Se algum atributo chegar a 0, o pet morre e nenhuma ação pode ser feita a não ser mostrar os dados.


class Tamagotchi:

    def __init__(self):
        self.nome = input("Dê um nome ao seu bixinho: ")
        self.energia = 100
        self.saciedade = 100
        self.limpeza = 100

        self.diamantes = 0
        self.idade = 0

    def mostrar_informacoes_pos_morte(self):
        print(f"Informações de {self.nome}:")
        print("Idade:",self.idade)
        print("Diamantes:",self.diamantes)
        print("Energia:",self.energia)
        print("Saciedade:",self.saciedade)
        print("Limpeza:",self.limpeza)

    def comendo(self):
        if self.saciedade == 0 or self.energia == 0 or self.limpeza == 0:
            print(f"{self.nome} morreu :(")
            return mostrar_informacoes_pos_morte()

        if self.saciedade == 100:
            print(f"{self.nome} não está com fome.")
            self.energia -= 5
            self.limpeza -= 10
            return True

        print(f"{self.nome} está comendo...")
        self.idade += 1
        self.saciedade += 20
        self.energia += 5
        
        self.limpeza -= 15
    
    def jogando(self):
        print(self.nome,"está jogando...")
        self.energia -= 20
        self.saciedade -= 25
        self.limpeza -= 30

        self.diamantes += 1
        self.idade += 1

    def dormindo(self):
        if self.energia >= 80:
            print(self.nome,"não está com sono.")
            return False
        print(self.nome,"está dormindo...")
        self.saciedade -= 50
        self.limpeza -= 40

        self.diamantes += 1
        self.idade += 1

        self.energia = 100

    
    def banho(self):
        if self.limpeza >= 80:
            print(self.nome,"não precisa tomar banho.")
            return False
        print(self.nome,"está tomando banho...")
        self.saciedade -= 20
        self.energia -= 20

        self.limpeza = 100
        self.diamantes += 1
        self.idade += 1
