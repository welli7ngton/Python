# Exercício 5: Verificador de horário de expediente
# Crie uma função chamada verifica_horario_expediente que receba uma data e
# hora como argumento e verifique se está dentro do horário de expediente de
# uma empresa (por exemplo, das 9h às 18h, de segunda a sexta-feira).
# A função deve retornar True se estiver no horário de
# expediente e False caso contrário.

import calendar
from datetime import datetime


def verifica_horario_expediente(data, hora):
    data_ = datetime.strptime(data + " | " + hora,  "%d/%m/%Y | %H:%M")

    nome_dia = calendar.day_name[calendar.weekday(data_.year,
                                                  data_.month,
                                                  data_.day)]
    print(nome_dia)
    if nome_dia in ["Sunday", "Saturday"]:
        print("Dia não é útil.")
        return False
    print("O dia é útil.")
    return True


if __name__ == "__main__":

    # print(calendar.monthcalendar(2023, 12))
    verifica_horario_expediente("26/12/2023", "07:57")
