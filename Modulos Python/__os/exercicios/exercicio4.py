# 4- Escreva um script que renomeie todos os arquivos de um
# diretório para adicionar um prefixo ao nome do arquivo.

import os

caminho_arquivo = "/home/welli7ngton/Desktop/TESTES"

for root, dirs, files in os.walk(caminho_arquivo):
    for file in files:
        caminho = f"{root}/{file}"
        os.rename(caminho, caminho.replace("WWW", ""))
