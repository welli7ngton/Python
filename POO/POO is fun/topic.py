# O objetivo dessa atividade é exercitar o que vocês aprenderam no cinema com
# algumas variações. Aqui, vamos implementar um sistema de alocação de
# passageiros em uma topic. Nossa topic tem uma quantidade máxima de
# passageiros, mas também define alguns assentos preferenciais.
# Intro

# Seu sistema deverá:

#     Inicializar e Mostrar.
#         Iniciar a topic solicitando a lotação máxima e a quantidade
#         de cadeiras preferenciais.
#         Mostrar o estado do trem:
#             Coloque @ na frente das cadeiras preferenciais
#             Coloque = na frente das cadeiras normais.
#     Inserir.
#         Inserir passageiros informando id e idade
#             Se o passageiro for idoso:
#                 Se houver cadeiras preferenciais
#                     O coloque na primeira cadeira preferência.
#             Senão
#                 O coloque na primeira cadeira normal.
#             Se o passageiro não for idoso.
#                 Se houver cadeiras não preferenciais
#                     O coloque na primeira não preferencial.
#                 Se não
#                     O coloque na primeira cadeira preferencial.
#     Remover.
#         Remover passageiros por id

# Existe uma lista para as cadeiras normais e outra para as preferenciais.
# Para facilitar nas operações de busca e inserção, você deverá criar vários
# métodos privados para simplificar a lógica dos métodos principais.

class Topic:

    def __init__(self, qtd_normal: int, qtd_preferencial: int) -> None:
        self.q_n = qtd_normal
        self.q_p = qtd_preferencial
        self.assentos = ["@" for x in range(qtd_preferencial)]
        self.preferencial = qtd_preferencial
        self.normal = qtd_normal
        self.prox_cadeira_n = qtd_preferencial
        self.prox_cadeira_p = 0
        for x in range(qtd_normal):
            self.assentos.append("=")
        # print(self.assentos)

    def __repr__(self) -> str:
        print("Assentos:")
        print(" ", ".|^^^|.")
        for i in range(0, len(self.assentos), 2):
            try:
                print("  |", self.assentos[i], self.assentos[i+1], "|")
            except IndexError:
                print("  |", self.assentos[len(self.assentos)-1], "  |")
        print(" ", "'-----'")
        return ""

    def inserir(self, id_: str, idade: int):
        # print(idade < 60 and self.normal == 0 and self.preferencial > 0)

        if self.normal == 0 and self.preferencial == 0:
            print("Não há vagas.")
            return False

        if idade >= 60 and self.preferencial > 0:
            self.assentos[self.prox_cadeira_p] = id_
            self.prox_cadeira_p += 1
            self.preferencial -= 1

        elif idade >= 60 and self.preferencial == 0:
            self.assentos[self.prox_cadeira_n] = id_
            self.prox_cadeira_n += 1
            self.normal -= 1

        elif idade < 60 and self.normal > 0:
            self.assentos[self.prox_cadeira_n] = id_
            self.prox_cadeira_n += 1
            self.normal -= 1

        elif idade < 60 and self.normal == 0 and self.preferencial > 0:
            self.assentos[self.prox_cadeira_p] = id_
            self.prox_cadeira_p += 1
            self.preferencial -= 1

    def remover(self, id_):
        # print(self.assentos)
        if id_ not in self.assentos:
            print("ID não está na topic.")
            return False

        for i in range(len(self.assentos)):
            if self.assentos[i] == id_:
                valor_assento = i
                break

        if valor_assento in range(0, self.q_p):
            self.assentos[valor_assento] = "@"
        else:
            self.assentos[valor_assento] = "="


t1 = Topic(5, 3)
# print(t1)

t1.inserir("1", 60)
t1.inserir("2", 60)
t1.inserir("3", 13)
t1.inserir("4", 12)
t1.inserir("5", 12)
t1.inserir("6", 12)
t1.inserir("7", 12)
t1.inserir("8", 12)
t1.inserir("8", 12)

print(t1)
t1.remover("10")
print(t1)
