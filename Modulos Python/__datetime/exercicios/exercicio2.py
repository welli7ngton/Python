# Exercício 2: Conversor de fusos horários
# Crie uma função chamada converte_fuso_horario que receba uma data e hora, um
# fuso horário de origem e um fuso horário de destino. A função deve retornar a
# data e hora convertidas para o fuso horário de destino.

from pytz import timezone
from datetime import datetime


def converte_fuso_horario(dia,
                          mes,
                          ano,
                          hora,
                          minut,
                          seg,
                          fuso_horario_origem,
                          fuso_horario_destino
                          ):
    fuso = timezone(fuso_horario_destino)
    data_formatada = datetime(day=dia,
                              month=mes,
                              year=ano,
                              hour=hora,
                              minute=minut,
                              second=seg,
                              tzinfo=fuso
                              )
    print(data_formatada)

if __name__ == "__main__":
    h = converte_fuso_horario(5, 5, 2023,
                              20, 4, 43,
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
