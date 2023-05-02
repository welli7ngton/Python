# Faça um programa que converta da notação de 24 horas para a notação de 12 horas

# o programa deveconverter 14:25 em 2:25 P.M. A entrada é dada em dois inteiros 

# A entrada é dada em dois inteiros. Deve haver pelo menos duas funções: 
#       uma para fazer a conversão
#       e uma para a saída.

# Registre a informação A.M./P.M. como um valor ‘A’ para A.M. e ‘P’ para P.M.

# Assim, a função para efetuar as conversões terá um parâmetro formal para registrar se é A.M. ou P.M.


# Inclua um loop que permita que o usuário repita esse cálculo para novos valores de entrada quantas vezes quiser.

c = 1
def novahora(hora):

    novahora = 0
    horario = ""

    if hora >= 13:
        novahora = hora - 12
        horario = "P"
        return(novahora,horario)
    elif hora <= 12:
        novahora = hora + 12
        horario = "A"
        return(novahora,horario)

def organizasaida(tupla,minuto):
    hora = int(tupla[0])
    amoupm = str(tupla[1])
    
    if amoupm == "P":
        print(f"a nova hora é: {hora}:{m} {amoupm}.M.")
    else:
        print(f"a nova hora é: {hora}:{m} {amoupm}.M.")

while c == 1:

    h = int(input("digite a hora: "))
    m = int(input("digite o minuto: "))

    tupla_horaetipo = novahora(h)

    organizasaida(tupla_horaetipo, m)

    c = int(input("deseja continuar? digite '1' para sim '0' para encerrar: "))