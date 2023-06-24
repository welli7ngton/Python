# Motoca

# Você já deve ter ido em algum parque e viu crianças de 4 a 10 anos andando naquelas motocas motorizadas. Pois é, nós vamos modelar e implementar uma delas.

# Intro
# Você deverá implementar a classe Pessoa e a class Moto.

# Iniciar
# A moto inicia com 1 de potência, sem minutos e sem ninguém.

# Subir
# Só pode estar uma pessoa na moto por vez. Para subir, informe nome e idade de quem está subindo.

# Descer
# Só pode descer se tiver alguém na moto.

# Comprar tempo
# O tempo em minutos é comprado e enquanto houver tempo, qualquer pessoa pode dirigir.

# Dirigir tempo
# Se houver uma pessoa com 10 anos ou menos e houver minutos, então ela pode passear de moto.
# Se o tempo acabar no meio do passeio, informe o quanto a pessoa andou.

# Buzinar
# Qualquer pessoa pode buzinar(honk)
# O barulho da buzina é “Pem”, porém o número de e é igual ao valor da potência.
# Ex: se a potência for 5, buzinar deve gerar: Peeeeem

import time

class Pessoa:

    def __init__(self,nome,idade,tempo_comprado=0):
        self.nome = nome
        self.idade = idade
        self.tempo_comprado = tempo_comprado
    
    def comprar_tempo(self,tempo):
        self.tempo_comprado = tempo
        print(f"{tempo} minutos compradoos.\n")
        return True

class Moto:
    
    def __init__(self,ocupada=False,potencia=1,minutos=0):
        self.ocupada = ocupada
        self.potencia = potencia
        self.minutos = 0
    
    def subir(self,other):
        if not self.ocupada:
            print(f"{other.nome} subiu.\n")
            return True
        else:
            print("A moto está ocupada.\n")
            return False

    def descer(self,other):
        if self.ocupada:
            print("Não tem ninguém na moto para descer.\n")
            return False
        else:
            print(f"{other.nome} desceu.\n")
            return True
    
    def comprar_tempo(self,other,tempo):
        other.tempo_comprado = tempo
        self.tempo = other.tempo_comprado
        print("Tempo comprado.\n")
        return True
    
    def dirigir(self,other):
        
        if self.tempo == 0:
            print("Sem tempo para andar na moto.\n")
            return False
        print(f"{other.nome} está dirigindo.\n")
        self.buzinar()
        c = 1
        while self.tempo != 0:
            time.sleep(1)
            print(f"Se passou {c} min.\n")
            c += 1
            self.tempo -= 1
        print("O passeio acabou.\n")     
        return True
    
    def buzinar(self):
        e = ""
        for i in range(self.potencia):
            e += "e"
        print(f"P{e}m!")

p = Pessoa("João",6)
m = Moto()
m.subir(p)
m.descer(p)
m.comprar_tempo(p,10)
m.subir(p)
m.dirigir(p)