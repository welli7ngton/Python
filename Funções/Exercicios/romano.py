# flake8:noqa
# Leia um número decimal (até 3	 dígitos) e	 escreva o	seu equivalente	 em
# numeração romana.	Utilize funções para obter cada dígito do número decimal e para a
# transformação de numeração decimal para romana (Dica1: 1 = I, 5 = V, 10 = X, 50 = L
# 100 =	C, 500 = D,	1.000 =	M;
# Dica2: utilize um	vetor guardando	a tradução para	
# cada um dos dígitos).
def obter_digito(numero, posicao):
    # Obtém o dígito na posição especificada da direita para a esquerda
    return (numero // 10**posicao) % 10

def decimal_para_romano(digito, unidade, cinco, dez):
    # Converte um dígito para numeração romana
    if digito == 9:
        return unidade + dez
    elif digito >= 5:
        return cinco + (unidade * (digito - 5))
    elif digito == 4:
        return unidade + cinco
    else:
        return unidade * digito

def converter_para_romano(numero):
    if numero < 1 or numero > 3999:
        return "Número fora do intervalo válido"

    romano = ""

    # Tradução dos dígitos
    unidades = ["", "I", "II", "III", "IV", "V", "VI", "VII", "VIII", "IX"]
    dezenas = ["", "X", "XX", "XXX", "XL", "L", "LX", "LXX", "LXXX", "XC"]
    centenas = ["", "C", "CC", "CCC", "CD", "D", "DC", "DCC", "DCCC", "CM"]

    # Obtém cada dígito do número decimal
    unidade = obter_digito(numero, 0)
    dezena = obter_digito(numero, 1)
    centena = obter_digito(numero, 2)

    # Converte cada dígito para numeração romana
    romano += centenas[centena]
    romano += dezenas[dezena]
    romano += unidades[unidade]

    return romano

# Obtém a entrada do usuário
numero_decimal = int(input("Digite um número decimal (até 3 dígitos): "))

# Converte para numeração romana e exibe o resultado
numero_romano = converter_para_romano(numero_decimal)
print(f"O número romano equivalente é: {numero_romano}")
