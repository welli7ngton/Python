# Exercício 3: Rastreador de datas importantes
# Crie uma classe chamada RastreadorDatas que receba uma lista de datas
# como argumento. A classe deve fornecer métodos para verificar se uma
# determinada data está presente na lista e para calcular a quantidade
# de dias entre a data atual e a próxima data da lista.

from datetime import datetime


class RastradorDatas:

    def __init__(self, lista_datas) -> None:
        self.lista_datas = [datetime.strptime(data, "%d/%m/%Y")
                            for data in lista_datas
                            ]

        # for data in self.lista_datas:
        #     print(type(data))

    def verifica_data(self, data: str):
        data = datetime.strptime(data, "%d/%m/%Y")
        if data in self.lista_datas:
            print("A data está entre a lista de datas importantes.")
            return True
        return False

    def calcula_dias(self):
        data_atual = datetime.now()
        time_stamp_atual = datetime.timestamp(data_atual)
        for data in self.lista_datas:
            if data < data_atual:
                continue
            else:
                proxima_data = data
                break
        delta = datetime.timestamp(proxima_data) - time_stamp_atual
        print(
            f"Faltam {int(delta //3600 // 24)} dias para a próxima data."
            )


r1 = RastradorDatas(["24/01/2023",
                     "13/06/2023",
                     "16/06/2023",
                     "07/12/2023",
                     "12/12/2023"])

r1.verifica_data("07/12/2023")
r1.calcula_dias()
