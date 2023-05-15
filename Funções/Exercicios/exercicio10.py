# Data com mês por extenso. Construa uma função que receba uma data no formato DD/MM/AAAA e devolva uma string no
# formato D de mesPorExtenso de AAAA. Opcionalmente, valide a data e retorne NULL caso a data seja inválida.


def convetedata(data):

    dia = ''
    mes = ''
    ano = ''

    dia = data[0:2] 
    ano = data[6:]
 
    

    if d[3] == '0' and d[4] == '1':
        mes = 'Janeiro'

    elif d[3] == '0' and d[4] == '2':
        mes = 'Fevereiro'

    elif d[3] == '0' and d[4] == '3':
        mes = 'Março'
                
    elif d[3] == '0' and d[4] == '4':
        mes = 'Abril'

    elif d[3] == '0' and d[4] == '5':
        mes = 'Maio'

    elif d[3] == '0' and d[4] == '6':
        mes = 'Junho'

    elif d[3] == '0' and d[4] == '7':
        mes = 'Julho'

    elif d[3] == '0' and d[4] == '8':
        mes = 'Agosto'

    elif d[3] == '0' and d[4] == '9':
        mes = 'Setembro'

    elif d[3] == '1' and d[4] == '0':
        mes = 'Outubro'

    elif d[3] == '1' and d[4] == '1':
        mes = 'Novembro'

    elif d[3] == '1' and d[4] == '2':
        mes = 'Dezembro'
    
    if int(data[0:2]) > 31 or int(data[3:5]) > 12:
        print("NULL")
    else:
        print(dia,mes,ano)



d = input("digite a data no formato DD/MM/AAA: ")

convetedata(d)