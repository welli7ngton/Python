# Exercício 9: Calculadora de tempo decorrido
# Crie uma função chamada calcula_tempo_decorrido que receba duas datas e
# horas como argumento e retorne o tempo decorrido entre elas,
# expresso em anos, meses, dias, horas, minutos e segundos.

from datetime import datetime


def calcula_tempo_decorrido(data1, data2):
    d1 = datetime.strptime(data1, "%d/%m/%Y %H:%M:%S")
    d2 = datetime.strptime(data2, "%d/%m/%Y %H:%M:%S")

    anos = d2.year - d1.year
    meses = d2.month - d1.month
    dias = d2.day - d1.day

    horas = d2.hour - d1.hour
    minutos = d2.minute - d1.minute
    segundos = d2.second - d1.second

    print("Anos:", anos)
    print("Meses:", meses)
    print("Dias:", dias)
    print("Horas:", horas)
    print("Minutos:", minutos)
    print("Segundos:", segundos)
    return True


if __name__ == "__main__":
    calcula_tempo_decorrido("25/4/2014 08:49:12", "26/4/2015 08:49:12")
