# Criando datas com módulo datetime
# datetime(ano, mês, dia)
# datetime(ano, mês, dia, horas, minutos, segundos)
# datetime.strptime('DATA', 'FORMATO')
# datetime.now()
# https://pt.wikipedia.org/wiki/Era_Unix
# datetime.fromtimestamp(Unix Timestamp)
# https://docs.python.org/3/library/datetime.html


from datetime import datetime

data_str = '03/07/2023'
data_str_forma = '%d/%m/%Y'


data = datetime.strptime(data_str, data_str_forma)
print(data)

print(datetime.now())
