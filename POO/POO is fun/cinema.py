# Cinema

# O objetivo dessa atividade é implementar o sistema de alocação de uma única
# sala de cinema. Se existem cadeiras livres, os clientes podem reservá-las.
# Também podem desistir da reserva. O sistema deve mostrar quem está sentado
# em cada cadeira.

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
# reservar uma cadeira para um cliente passando id, telefone e número da
# cadeira avise que houve erro ao tentar colocar duas pessoas na mesma cadeira.
# avise que houve erro ao tentar colocar duas pessoas com mesmo id na sala.
# atualize a função show para mostrar os clientes onde estiverem sentados.

# Cancelamentos.
# Cancele reserva passando o id do cliente.

from random import randint


class Cliente:

    def __init__(self, nome: str, idade: int, telefone: str):
        self.nome = nome
        self.idade = idade
        self.telefone = telefone
        self._id = randint(100, 1000)
        self.reserva = False
        self.cadeira = None

    def __repr__(self) -> str:
        return f"ID: {self._id} | {self.nome}, {self.idade} anos. "

    @property
    def get_nome(self):
        return self.nome

    @get_nome.setter
    def get_nome(self, valor):
        self.nome = valor

    @property
    def get_idade(self):
        return self.idade

    @get_idade.setter
    def get_idade(self, valor):
        self.idade = valor

    @property
    def get_telefone(self):
        return self.telefone

    @get_telefone.setter
    def get_telefone(self, valor):
        self.telefone = valor


class SalaCinema:

    def __init__(self):
        self.vagas = 30
        self.ocupadas = []

    def fazer_reserva(self, cliente: Cliente, id: int, num_cadeira: int):
        if cliente.reserva:
            print("O cliente ja tem uma reserva.")
            return False
        elif num_cadeira in self.ocupadas:
            print("Cadeira ja ocupada.")
            return False
        cliente.reserva = True
        cliente.cadeira = num_cadeira
        self.ocupadas.append(num_cadeira)
        self.vagas -= 1
        print("Reserva concluída.")
        return True


if __name__ == "__main__":

    cinema = SalaCinema()

    c1 = Cliente("Jose Freitas", 18, "88 9 8888-8888")
    c2 = Cliente("Wellington Almeida", 20, "88 9 9999-9999")
    c3 = Cliente("Maria Helena", 20, "88 9 1111-1111")
    c4 = Cliente("Rian Marlom", 19, "88 9 7777-7777")

    cinema.fazer_reserva(c1, c1._id, 13)
    cinema.fazer_reserva(c2, c2._id, 14)
    cinema.fazer_reserva(c3, c3._id, 15)
    cinema.fazer_reserva(c4, c4._id, 16)
    print(cinema.ocupadas)
