# Exercício 2: Conversor de fusos horários
# Crie uma função chamada converte_fuso_horario que receba uma data e hora, um
# fuso horário de origem e um fuso horário de destino. A função deve retornar a
# data e hora convertidas para o fuso horário de destino.

from pytz import timezone
from datetime import datetime


def converte_fuso_horario(data,
                          hora,
                          fuso_horario_origem,
                          fuso_horario_destino
                          ):
    data_origem = datetime.strptime(data + "-" + hora, "%d/%m/%Y-%H:%M:%S")

    return data_origem.astimezone(timezone(fuso_horario_destino))


if __name__ == "__main__":
    h = converte_fuso_horario("05/05/2023",
                              "21:8:43",
                              "America/Fortaleza",
                              "Asia/Tokyo")

    print(h)

    # testes usando o horario atual
    # print(datetime.now(
    #     timezone("Asia/Tokyo")).strftime("%d/%m/%Y - %H:%M:%S")
    #     )
    # print(datetime.now(
    #     timezone("America/Sao_Paulo")).strftime("%d/%m/%Y - %H:%M:%S")
    #     )
