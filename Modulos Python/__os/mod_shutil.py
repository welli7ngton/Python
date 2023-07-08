# os + shutil - Copiando arquivos com Python
# Vamos copiar arquivos de uma pasta para outra.
# Copiar -> shutil.copy

import os
import shutil


HOME = os.path.expanduser("~")
DESKTOP = os.path.join(HOME, "Desktop")
# desktop
# print(DESKTOP)
# home
# print(HOME)

caminho_exemplo = os.path.join(DESKTOP, "EXEMPLO")
# print(caminho_exemplo)
os.system(f"cd {caminho_exemplo}")
# for root, dirs, files in os.walk(caminho_exemplo):
#     print(root)
#     print(dirs)
#     print(files)

caminho_nova_pasta = os.path.join(DESKTOP, "NOVA_PASTA")
os.makedirs(caminho_nova_pasta, exist_ok=True)

for root, dirs, files in os.walk(caminho_exemplo):
    os.makedirs(root.replace("EXEMPLO", "NOVA_PASTA"), exist_ok=True)

for root, dirs, files in os.walk(caminho_exemplo):
    for file in files:
        caminho_arquivo = os.path.join(root, file)
        # print(caminho_arquivo)
        caminho_novo_arquivo = os.path.join(
            caminho_arquivo.replace("EXEMPLO", "NOVA_PASTA")
            )
        print(caminho_novo_arquivo)
        shutil.copy(caminho_arquivo, caminho_novo_arquivo)
