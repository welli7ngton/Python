# 8- Escreva um script que exclua todos os arquivos em um diretório
# mantendo os diretórios intactos.

import os

HOME = os.path.expanduser("~")

HOME += os.path.join("/Desktop", "TESTES2")

for root, dirs, files in os.walk(HOME):
    for file in files:
        if os.path.isfile(root+"/"+file):
            os.unlink(root+"/"+file)
