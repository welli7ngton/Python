# Exercício 1: Calculadora de dias úteis
# Crie uma classe chamada CalculadoraDiasUteis que receba uma data de
# início e uma quantidade de dias como argumentos. A classe deve fornecer
# um método para calcular a data final considerando apenas dias úteis
# (excluindo sábados e domingos).

from datetime import datetime
from dateutil.relativedelta import relativedelta


class CalculadoraDiasUteis:

    def __init__(self, dia: int, mes: int, ano: int, qtd_dias: int) -> None:
        self.dia = dia
        self.mes = mes
        self.ano = ano
        self.qtd_dias = qtd_dias

    def __repr__(self) -> str:
        data_formatada = datetime.strftime(self.data, "%d/%m/%Y")
        return f"{data_formatada}"

    def calcular_data(self):

        self.data = datetime(day=self.dia, month=self.mes, year=self.ano)

        for i in range(0, self.qtd_dias+1):
            if i % 5 == 0:
                self.data += relativedelta(days=+2)
            else:
                self.data += relativedelta(days=+1)

        data_formatada = datetime.strftime(self.data, "%d/%m/%Y")
        return f"{data_formatada}"


d1 = CalculadoraDiasUteis(3, 5, 2023, 10)
print(d1.calcular_data())
