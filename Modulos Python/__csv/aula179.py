# csv.reader e csv.DictReader
# csv.reader lê o CSV em formato de lista
# csv.DictReader lê o CSV em formato de dicionário

import csv
from pathlib import Path

caminho_csv = Path(__file__).parent / "aula179.csv"

print()
# leitor no modo lista
with open(caminho_csv, "r") as arq:
    leitor = csv.reader(arq)
    for linha in leitor:
        print(linha)
    print()

# leitor no modo de dicionário
with open(caminho_csv, "r") as arq:
    leitor = csv.DictReader(arq)
    for linha in leitor:
        print(linha)
    print()
