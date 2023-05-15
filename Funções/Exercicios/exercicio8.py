# crie umprograma que use a função valorPagamento para determinar o valor a ser pago por uma prestação de uma conta.

# O programa deverá solicitar ao usuário o valor da prestação e o número de dias em atraso e passar estes
# valores para a função valorPagamento, que calculará o valor a ser pago e devolverá este valor ao programa 
# que a chamou.

# O programa deverá então exibir o valor a ser pago na tela. Após a execução o programa deverá
# voltar a pedir outro valor de prestação e assim continuar até que seja informado um valor igual a zero
# para a prestação

# Neste momento o programa deverá ser encerrado, exibindo o relatório do dia
# que conterá a quantidade e o valor total de prestações pagas no dia.

# O cálculo do valor a ser pagoé feito da seguinte forma. Para pagamentos sem atraso, cobrar o valor da prestação.
# Quando houver atraso, cobrar 3% de multa, mais 0,1% de juros por dia de atraso.

relatorio = []
prestacao = 1
def valorpagamento(v_prestacao,dias_atraso):
    vpago = 0
    multa = v_prestacao * 0.03
    juros = 0.01 * dias_atraso
    if dias_atraso == 0:
        vpago = v_prestacao
    else:
        vpago = v_prestacao + multa + juros
    relatorio.append(vpago)
    print(f"o valor a ser pago é: {vpago}")
    

while True:
    prestacao = int(input("digite o valor da prestação: "))
    if prestacao == 0:
        break
    atraso = int(input("digite a quantidade de dias atrasados: "))

    valorpagamento(prestacao, atraso)

print(f"a quantidade de parcelas pagas foi: {len(relatorio)}")

print(f"e o valor total pago foi: {sum(relatorio)}")


