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

    funcionando = False

    def __init__(self):
        self.hora = 0
        self.min = 0
        self.seg = 0
        
    def ajusta_hora(self,hora,minuto,segundo):
        if segundo >= 60 or minuto >= 60 or hora >=24:
            print("Valor inválido.")
            return False
        self.hora = hora
        self.min = minuto
        self.seg = segundo
    
    def mostra_hora(self):
        print(f"{self.hora}:{self.min}:{self.seg}")
    
    @classmethod
    def conta_tempo(self,hora=self.hora,minuto=self.min,segundo=self.seg):
        while True:
            for i in range(0,59):
                time.sleep(1)
                segundo += 1
            minuto += 1
            if minuto == 60 and hora <= 12:
                minuto = 0
                hora += 1
                return hora,minuto,segundo
            elif hora == 12:
                hora = 0
                minuto = 0
                segundo = 0
                return hora,minuto,segundo

    self.hora, self.min,self.seg = conta_tempo()


r1 = Relogio()

r1.ajusta_hora(21, 4, 32)

r1.mostra_hora()