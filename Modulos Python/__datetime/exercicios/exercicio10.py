# Exercício 10: Contador regressivo para o ano novo
# Crie uma classe chamada ContadorRegressivoAnoNovo que inicie um contador
# regressivo para o próximo ano novo. A classe deve fornecer um método para
# exibir o tempo restante até a virada do ano, atualizado a cada segundo.

from datetime import datetime
import time


class ContadorRegressivoAnoNovo:

    def __init__(self) -> None:
        virada = datetime(year=2024,
                          month=1,
                          day=1,
                          hour=0,
                          minute=0,
                          second=0)

        while datetime.now() <= virada:
            delta = datetime.timestamp(virada)\
                - datetime.timestamp(datetime.now())
            print(f"Faltam {delta:.0f}s para o Rei velhão")
            time.sleep(1)


if __name__ == "__main__":
    c1 = ContadorRegressivoAnoNovo()
