# os + shutil - Copiando arquivos com Python
# Vamos copiar arquivos de uma pasta para outra.
# Copiar -> shutil.copy

import os
import shutil


HOME = os.path.expanduser("~")
DESKTOP = os.path.join(HOME, "Área de Trabalho")
print(DESKTOP)
