# 10 -Escreva um script que mova todos os arquivos de um diretório
# para outro diretório, excluindo o diretório de origem.

import os
from _home import HOME
import shutil


def mover_arquivos(origem, destino):
    if not os.path.exists(destino):
        os.makedirs(destino)

    arquivos = os.listdir(origem)

    for arquivo in arquivos:
        caminho_origem = os.path.join(origem, arquivo)
        caminho_destino = os.path.join(destino, arquivo)

        shutil.move(caminho_origem, caminho_destino)

    print("Arquivos movidos com sucesso!")


diretorio_origem = os.path.join(HOME, "TESTES123")
diretorio_destino = os.path.join(HOME, "TESTES")

mover_arquivos(diretorio_origem, diretorio_destino)
os.rmdir(diretorio_origem)
