# 12- Escreva um script que calcule o tamanho total ocupado por todos
# os arquivos em um diretório específico.

from _home import HOME
import os
import math


def formata_tamanho(tamanho_em_bytes: int, base: int = 1000):

    if tamanho_em_bytes <= 0:
        return "0B"

    abreviacao_tamanhos = "B", "KB", "MB", "GB", "TB", "PB"
    indice_abreviacao_tamanhos = int(math.log(tamanho_em_bytes, base))
    potencia = base ** indice_abreviacao_tamanhos
    tamanho_final = tamanho_em_bytes / potencia
    abreviacao_tamanho = abreviacao_tamanhos[indice_abreviacao_tamanhos]

    print(f"{tamanho_final:.1f} {abreviacao_tamanho}")


tamanho = 0
for root, dirs, files in os.walk(HOME):
    for file in files:
        tamanho += os.path.getsize(os.path.join(root, file))

print(f"{tamanho:,.0f} B")
formata_tamanho(tamanho)
