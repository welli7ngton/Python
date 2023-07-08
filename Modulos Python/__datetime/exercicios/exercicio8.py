# Exercício 8: Verificador de aniversário próximo
# Crie uma classe chamada VerificadorAniversario que receba a data de
# nascimento de uma pessoa e forneça um método para verificar se o aniversário
# está próximo (por exemplo, nos próximos 30 dias). A classe também deve
# fornecer um método para calcular a quantidade de dias restantes até o
# próximo aniversário.

from datetime import datetime


class VerificadroAniversario:

    def __init__(self) -> None:
        pass

    def verifica_proximidade(self, aniversario):
        data_atual = datetime.now()
        aniversario_ = datetime.strptime(aniversario, "%d/%m/%Y")
        tsp_atual = datetime.timestamp(data_atual)
        tsp_nasc = datetime.timestamp(aniversario_)

        if (tsp_nasc - tsp_atual)//86400 <= 30:
            print(f"Está proximo: {(tsp_nasc-tsp_atual)//86400:.0f} dias.")
            return True
        print(f"Não está próximo: {(tsp_nasc-tsp_atual)//86400:.0f} dias.")
        return False

    def calcula_dias_prox_ani(self, data):
        data_ = datetime.strptime(data, "%d/%m/%Y")
        data_atual = datetime.now()
        delta = datetime.timestamp(data_)-datetime.timestamp(data_atual)
        print(f"Faltam {delta//86400:.0f} dias para seu próximo aniversário.")


if __name__ == "__main__":
    v1 = VerificadroAniversario()
    v1.verifica_proximidade("07/8/2023")
    v1.calcula_dias_prox_ani("07/12/2025")
