# 9- Crie um programa que copie todos os arquivos de um diretório
# para outro diretório especificado pelo usuário.

import os
import shutil

HOME = os.path.expanduser("~")

HOME += os.path.join("/Desktop")

# pasta1 = input("Digite o nome da pasta que quer copiar: ")
# pasta2 = input("Digite o nome da pasta que quer colar: ")

caminho_p1 = HOME+"/"+'TESTES'
caminho_p2 = HOME+"/"+'TESTES23'

if os.path.isdir(caminho_p1) and os.path.isdir(caminho_p2):
    for root, dirs, files in os.walk(caminho_p1):
        for dir_ in dirs:
            for file in files:
                print(os.path.isfile(root+"/"+file))
                shutil.copy(root+"/"+file, caminho_p2)

    print("Arquivos copiados.")
else:
    print("Caminhos não encontrados.")
    print(caminho_p1)
    print(caminho_p2)
