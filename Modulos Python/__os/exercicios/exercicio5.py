# 5- Crie um programa que liste todos os subdiretórios em
# um diretório especificado.

import os

caminho_diretorio = os.path.expanduser("~")

caminho_diretorio += os.path.join("/Desktop", "Github", "Python")
print(caminho_diretorio)

print(os.path.isdir(caminho_diretorio))

for root, dirs, files in os.walk(caminho_diretorio):
    print(dirs)
