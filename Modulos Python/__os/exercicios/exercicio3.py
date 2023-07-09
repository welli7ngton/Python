# 3- Crie um programa que verifique se um arquivo
# existe em um diretório específico.

import os

caminho_arquivo = "/home/welli7ngton/Desktop/TESTES"

nome = input("Digite o nome do arquivo: ")

print(os.path.isfile(os.path.join(f"{caminho_arquivo}/{nome}")))
