# Exercício 6: Calculadora de idade em dias
# Crie uma classe chamada CalculadoraIdadeDias que receba a data de nascimento
# de uma pessoa e forneça um método para calcular a idade atual em dias.

from datetime import datetime


class CalculadoraIdadeDias:

    def __init__(self) -> None:
        self.data_atual = datetime.now()

    def calcula_idade(self, nascimento):
        data = datetime.strptime(nascimento, "%d/%m/%Y")
        # print(data)

        data_atutual = datetime.timestamp(self.data_atual)
        ano_nas = datetime.timestamp(data)

        print(f"Idade em dias: {(data_atutual - ano_nas)//(3600*24):.0f}")


if __name__ == "__main__":

    c1 = CalculadoraIdadeDias()
    c1.calcula_idade("07/12/2002")
