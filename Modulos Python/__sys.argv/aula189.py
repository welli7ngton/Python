# argparse.ArgumentParser para argumentos mais complexos
# Tutorial Oficial:
# https://docs.python.org/pt-br/3/howto/argparse.html

from argparse import ArgumentParser

parser = ArgumentParser()

parser.add_argument("-b",
                    "--basic",
                    help="Mostra 'Olá Mundo' na tela",
                    type=str,
                    metavar="STRING",
                    # default="Olá mundo" deixa Olá mundo como valor padrão
                    required=False,
                    action="append"  # recebe o argumento mais de uma vez
                    # nargs="+" recebe mais de um valor e cria uma lista
                    )

args = parser.parse_args()




















