# 1- Crie um programa que liste todos os arquivos em um diretório
# especificado pelo usuário.

import os

HOME = os.path.expanduser("~")
HOME += os.path.join("/Desktop")


diretorio = input("Digite o nome do diretório: ")

HOME += os.path.join(f"/{diretorio}")
if not os.path.isdir(HOME):
    print(diretorio, "Não é um diretório.")
    pass
for root, dirs, files in os.walk(HOME):
    for file in files:
        print(file)
        print(root)
for root, dirs, files in os.walk(HOME):
    print(dirs)
for root, dirs, files in os.walk(HOME):
    print(root)
