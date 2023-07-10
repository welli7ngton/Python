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
arquivos = os.listdir(HOME)
for arq in arquivos:
    print("Arquivos")
    print(arq)
# for root, dirs, files in os.walk(HOME):
#     for file in files:
#         print(os.path.join(root, file))
