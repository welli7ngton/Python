# ZIP - Compactando / Descompactando arquivos com zipfile.ZipFile
import os
from pathlib import Path
from zipfile import ZipFile

# Caminhos
CAMINHO_RAIZ = Path(__file__).parent
CAMINHO_ZIP_DIR = CAMINHO_RAIZ / 'aula_186_diretorio_zip'
CAMINHO_COMPACTADO = CAMINHO_RAIZ / 'aula186_compactado.zip'
CAMINHO_DESCOMPACTADO = CAMINHO_RAIZ / 'aula186_descompactado'


# Cria o diretório para a aula
CAMINHO_ZIP_DIR.mkdir(exist_ok=True)


def criar_arquivos(qtd: int, zip_dir: Path):
    for i in range(qtd):
        texto = 'arquivo_%s' % (i + 1)
        with open(zip_dir / f'{texto}.txt', 'w') as arquivo:
            arquivo.write(texto)


criar_arquivos(10, CAMINHO_ZIP_DIR)

# criando zip e adicionando arquivos
with ZipFile(CAMINHO_COMPACTADO, "w") as zip:
    for root, dirs, files in os.walk(CAMINHO_ZIP_DIR):
        for file in files:
            # print(file)
            zip.write(os.path.join(root, file), file)

# lendo zip
with ZipFile(CAMINHO_COMPACTADO, "r") as zip:
    for arq in zip.namelist():
        print(arq)

# desempacotando zip
with ZipFile(CAMINHO_COMPACTADO, "r") as zip:
    zip.extractall(CAMINHO_DESCOMPACTADO)
