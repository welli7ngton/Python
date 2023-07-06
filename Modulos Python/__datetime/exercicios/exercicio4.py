# Exercício 4: Contador regressivo para eventos
# Crie uma classe chamada ContadorRegressivo que receba uma data e hora
# de um evento como argumento. A classe deve fornecer um método para iniciar
# um contador regressivo que exiba o tempo restante até o evento, atualizado a
# cada segundo.

from datetime import datetime
import time


class ContadorRegressivo:

    def __init__(self, data, hora) -> None:
        self.data = datetime.strptime(data + " | " + hora,
                                      "%d/%m/%Y | %H:%M:%S")

    def contador_regressivo(self):
        # print(datetime.timestamp(self.data), self.data)
        # print(datetime.timestamp(datetime.now()),  datetime.now())
        while True:
            delta = datetime.timestamp(self.data) -\
                 datetime.timestamp(datetime.now())
            print(f"Faltam {int(delta)}s.")
            delta = datetime.timestamp(self.data) -\
                datetime.timestamp(datetime.now())
            time.sleep(1)
            if delta <= 0:
                break

    def contador(self):

        while True:
            if datetime.now() >= self.data:
                print("A hora do evento chegou.")
                print(datetime.strftime(datetime.now(), "%d/%m/%Y | %H:%M:%S"))
                break
            time.sleep(1)
            print(datetime.strftime(datetime.now(), "%d/%m/%Y | %H:%M:%S"))


c = ContadorRegressivo("06/07/2023", "20:49:55")
# c.contador()
c.contador_regressivo()
