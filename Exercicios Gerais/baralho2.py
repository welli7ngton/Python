# https://olimpiada.ic.unicamp.br/pratique/ps/2021/f1/baralho/


def divide_naipes(lista_dados):
    C = [dado for dado in lista_dados if "C" in dado]
    E = [dado for dado in lista_dados if "E" in dado]
    U = [dado for dado in lista_dados if "U" in dado]
    P = [dado for dado in lista_dados if "P" in dado]

    return C, E, U, P


def verifica_iguais(lista_cartas, pos=0):
    if pos > len(lista_cartas) or len(lista_cartas) == 0:
        return True
    carta = lista_cartas.pop(0)
    if carta in lista_cartas:
        return False

    lista_cartas.append(carta)
    pos += 1

    return verifica_iguais(lista_cartas, pos)


def retorna_falta(cartasX):
    if not verifica_iguais(cartasX):
        return "erro"

    return 13 - len(cartasX)


dados = input()
lista_dados = []

for i in range(0, len(dados), 3):
    lista_dados.append(dados[i : i + 3])

cartasC, cartasE, cartasU, cartasP = divide_naipes(lista_dados)

print(retorna_falta(cartasC))
print(retorna_falta(cartasE))
print(retorna_falta(cartasU))
print(retorna_falta(cartasP))

