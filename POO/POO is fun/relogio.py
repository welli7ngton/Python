# Relógio
# Utilizando os comandos set para manter a hora correta

# O sistema deverá:

# Gerenciar uma classe que guarda a hora, minuto e segundo.
# Ao iniciar a classe, hora, minuto e segundo devem ser setados para 0.
# O construtor deve receber 3 parâmetros, hora, minuto e segundo.
# Para fazer a inicialização dos 3 parâmetros, utilize os métodos set.
# Crie os métodos getters e setters para cada atributo.
# Os métodos set devem garantir que os valores atribuúido sempre seja válido, ou não realize nenhuma mudança.
# Crie um método que imprime a hora no formato HH:MM:SS.
# Crie um método que incrementa o segundo em 1.

import time

class Relogio:
    def __init__(self, hora=0, minuto=0, segundo=0):
        self.__hora = self.set_hora(hora)
        self.__minuto = self.set_minuto(minuto)
        self.__segundo = self.set_segundo(segundo)

    def get_hora(self):
        return self.__hora

    def get_minuto(self):
        return self.__minuto

    def get_segundo(self):
        return self.__segundo

    def set_hora(self, hora):
        if 0 <= hora < 24:
            return hora
        else:
            return self.__hora

    def set_minuto(self, minuto):
        if 0 <= minuto < 60:
            return minuto
        else:
            return self.__minuto

    def set_segundo(self, segundo):
        if 0 <= segundo < 60:
            return segundo
        else:
            return self.__segundo

    def imprimir_hora(self):
        print(f"{self.__hora:02d}:{self.__minuto:02d}:{self.__segundo:02d}")

    def incrementar_segundo(self):
        self.__segundo += 1
        if self.__segundo == 60:
            self.__segundo = 0
            self.incrementar_minuto()

    def incrementar_minuto(self):
        self.__minuto += 1
        if self.__minuto == 60:
            self.__minuto = 0
            self.incrementar_hora()

    def incrementar_hora(self):
        self.__hora += 1
        if self.__hora == 24:
            self.__hora = 0

r = Relogio()

for a in range(300):
    r.incrementar_segundo()
    r.imprimir_hora()