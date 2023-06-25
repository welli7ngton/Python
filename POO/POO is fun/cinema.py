# Cinema

# O objetivo dessa atividade é implementar o sistema de alocação de uma única sala de cinema. Se existem cadeiras livres, os clientes podem reservá-las. Também podem desistir da reserva. O sistema deve mostrar quem está sentado em cada cadeira.

# Nessa atividade, você deverá criar:

# Uma classe que representa o cliente.
# Uma classe que representa a sala de cinema e guarda os clientes.

# Intro
# Seu sistema deverá:

# Inicializando.
# Iniciar a sala de cinema.
# Ao iniciar, você deve informar quantos assentos existem na sua sala.
# Mostrar o estado da sala, escrevendo um - para cada cadeira vazia.
# Se uma nova sala for iniciada, apague todas as informações da sala antiga.

# Reservas.
# reservar uma cadeira para um cliente passando id, telefone e número da cadeira.
# avise que houve erro ao tentar colocar duas pessoas na mesma cadeira.
# avise que houve erro ao tentar colocar duas pessoas com mesmo id na sala.
# atualize a função show para mostrar os clientes onde estiverem sentados.

# Cancelamentos.
# Cancele reserva passando o id do cliente.

import random

class Cliente:
    
    def __init__(self,nome,idade,telefone):
        self.nome = nome
        self.idade = idade
        self.telefone = telefone

    def infor_reserva(self):
        nome = self.nome
        telefone = self.telefone
        self.id_ =  random.randint(10,99)
        self.num_cadeira = random.randint(10,99)

        return nome,telefone,self.id_,self.num_cadeira


    def __repr__(self):
        return f"{self.nome!r}"

class Cinema:

    def __init__(self):
        self.vagas = 100
        self.ocupadas = 0
        self.num_cadeiras = []
        
    def reserva(self,other):
        nome,tel,id_,num_cadeira = other.infor_reserva()
        print("Dados da reserva:")
        print(f"Nome: {nome}")
        print(f"Telefone: {tel}")
        print(f"ID: {id_}")
        print(f"Cadeira: {num_cadeira}")
        self.vagas -=1
        self.ocupadas +=1
        self.num_cadeiras.append(num_cadeira)

    


