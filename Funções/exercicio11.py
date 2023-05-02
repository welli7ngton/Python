#Embaralha palavra. Construa uma função que receba uma string como parâmetro e devolva outra string com
#os carateres embaralhados. Por exemplo: se função receber a palavra python, pode retornar npthyo, ophtyn
#ou qualquer outra combinação possível, de forma aleatória. Padronize em sua função que todos os caracteres
#serão devolvidos em caixa alta ou caixa baixa, independentemente de como foram digitados.

import random

def embaralha(palavra):
    # transforma a palavra em uma lista de caracteres
    lista_chars = list(palavra)
    # embaralha a lista usando a função random.sample()
    nova_lista = random.sample(lista_chars, len(lista_chars))
    # junta os caracteres da lista em uma nova string
    nova_palavra = ''.join(nova_lista)
    # padroniza a caixa da nova palavra

    print(nova_palavra.upper())

p = input("digite a palavra: ")


embaralha(p)