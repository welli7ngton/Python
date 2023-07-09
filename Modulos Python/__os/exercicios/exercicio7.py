# 7- Crie um programa que liste todos os arquivos de um diretório e seus
# subdiretórios, exibindo o caminho completo de cada arquivo.

import os

HOME = os.path.expanduser("~")

HOME += os.path.join("/Desktop", "TESTES")

# print(os.path.isdir(HOME))
# print(HOME)

for root, dirs, files in os.walk(HOME):
    print("\nCaminho raiz:", root, "\n")
    print("Arquivos:")
    for file in files:
        caminho_arq = HOME + os.path.join("/"+file)
        print(caminho_arq)
