from pathlib import Path
import csv

caminho_csv = Path(__file__).parent / "aula180.csv"

# lista com os dicionários das informações
lista_clientes = [
    {"Nome": "Luiz Otávio", "Endereco": "Rua 1"},
    {"Nome": "Wellington", "Endereco": "Rua 2"},
    {"Nome": "Maria Helena", "Endereco": "Rua 3"},
    {"Nome": "Rian", "Endereco": "Rua 4"},
]

with open(caminho_csv, "w") as arq:
    # pegando as chaves do dicionário
    chaves = lista_clientes[0].keys()

    # criando escritor
    escritor = csv.writer(arq)
    # escrevendo a primeira linha com as chaves
    escritor.writerow(chaves)
    # escrevendo os dados de cada cliente no csv
    for cliente in lista_clientes:
        escritor.writerow(cliente.values())
