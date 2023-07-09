# 2- Escreva um script que crie uma nova pasta chamada "Backup"
# e copie todos os arquivos de um diretório específico para essa pasta.

import os
import shutil

caminho_diretorio = "/home/welli7ngton/Desktop/TESTES"

caminho_backup = caminho_diretorio.replace("TESTES", "BACKUP")

# print(caminho_backup)


for root, dirs, files in os.walk(caminho_diretorio):
    os.makedirs(root.replace("TESTES", "BACKUP"), exist_ok=True)
    for file in files:
        shutil.copy(f"{root}/{file}", root.replace("TESTES", "BACKUP"))
        print(file, "copiado.")
