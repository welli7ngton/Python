# 13- Crie um programa que liste os arquivos em um diretório
# por ordem de tamanho, do maior para o menor.

import os
from _home import HOME


def organiza_tamanhos(lista_tamanhos):
    lista_tamanhos.sort(reverse=True)
    return lista_tamanhos


tamanhos = []
caminho_tamanho = {}
for root, firs, files in os.walk(HOME):
    for file in files:
        caminho_tamanho[
            os.path.getsize(os.path.join(root, file))
            ] = os.path.join(root, file)

        tamanhos.append(os.path.getsize(os.path.join(root, file)))

    tamanhos = organiza_tamanhos(tamanhos)

for tam in tamanhos:
    print(caminho_tamanho[tam], tam)
