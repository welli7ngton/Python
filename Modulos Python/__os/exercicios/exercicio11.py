# 11- Crie um programa que conte o número total de arquivos em um
# diretório e seus subdiretórios.

import os
from _home import HOME

# print(os.path.isdir(HOME))

conta_arq = 0

for root, dirs, files in os.walk(HOME):
    for file in files:
        print(os.path.join(root, file))
        if os.path.isfile(os.path.join(root, file)):
            conta_arq += 1

print("\nO total de arquivos encontrados é:", conta_arq)
