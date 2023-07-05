# Exercício solucionado: calculando as datas e parcelas de um empréstimo
# Maria pegou um empréstimo de 1.000.000
# para realizar o pagamento em 5 anos.
# A data em que ela pegou o empréstimo foi
# 20/12/2020 e o vencimento de cada parcela
# é no dia 20 de cada mês.
# - Crie a data do empréstimo
# - Crie a data do final do empréstimo
# - Mostre todas as datas de vencimento e o valor de cada parcela

from datetime import datetime
from dateutil.relativedelta import relativedelta

valor_total = 1_000_000
data_emprestimo = datetime(2020, 12, 20)
data_final = data_emprestimo + relativedelta(years=5)

data_parcela = data_emprestimo
lista_parcelas = []


while data_parcela < data_final:
    lista_parcelas.append(data_parcela)
    data_parcela += relativedelta(months=+1)

num_parcelas = len(lista_parcelas)
valor_parcelas = valor_total/num_parcelas

for i in lista_parcelas:
    print(datetime.strftime(i, "%d/%m/%Y"), f"R$ {valor_parcelas:,.2f}")

print()
print(
    f"Você pegou R${valor_total:,.2f} para pagar "
    f"em 5 anos "
    f"({num_parcelas} meses) em parcelas de "
    f"R${valor_parcelas:,.2f}"
)
