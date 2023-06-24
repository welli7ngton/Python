# Pula pula
# Nosso objetivo no trabalho é modelar um gestor de pula pulas em um parquinho, controlando as pessoas que entram e saem do pula pula, além de coordenar as pessoas que estão na fila de espera.

# Intro
# Inserir crianças na fila de espera do pula pula
# Mover a primeira criança da fila de espera do pula pula para dentro do pula pula.
# Mover a primeira criança que entrou no pula pula para o final da fila de espera.


class Pulapula:

    def __init__(self):
        self.qtd_criancas = 0
        self.fila = []
        self.no_pulapula = []

    def add_crianca_fila(self,other):
        self.fila.append(other)
        print(f"{other.nome} entrou na fila.")
        return True
    
    def add_crianca_pulapula(self):
        if self.qtd_criancas < 4:
            self.qtd_criancas += 1
            print(f"{self.fila[0].nome} entrou no Pula Pula.")
            self.no_pulapula.append(self.fila.pop(0))
            return True
        print("Aguarde uma criança sair para deixar outra criança entrar.")
        return False

    def remove_crianca(self):
        print(f"{self.no_pulapula[0].nome} foi para o final da fila.")
        self.fila.append(self.no_pulapula.pop(0))
        self.qtd_criancas -= 1
        return True
    
        

class Crianca:

    def __init__(self,nome,idade):
        self.nome = nome
        self.idade = idade
c1 = Crianca("Joao",8)    
c2 = Crianca("Maria",5)    
c3 = Crianca("Jose",4)    
c4 = Crianca("Helena",4)    
c5 = Crianca("Tiago",8)    
c6 = Crianca("Rian",5)    
c7 = Crianca("Leonardo",7)   

p1 = Pulapula()

p1.add_crianca_fila(c1)
p1.add_crianca_fila(c2)
p1.add_crianca_fila(c3)
p1.add_crianca_fila(c4)
p1.add_crianca_fila(c5)
p1.add_crianca_fila(c6)
p1.add_crianca_fila(c7)

print()

p1.add_crianca_pulapula()
p1.add_crianca_pulapula()
p1.add_crianca_pulapula()
p1.add_crianca_pulapula()
p1.add_crianca_pulapula()

print()

p1.remove_crianca()
p1.add_crianca_pulapula()
p1.remove_crianca()
p1.add_crianca_pulapula()
p1.add_crianca_pulapula()
p1.remove_crianca()
p1.remove_crianca()
p1.add_crianca_pulapula()
p1.add_crianca_pulapula()
