# sys.argv - executando arquivos com argumentos no sistema
# fonte = Fira Code

import sys


args = sys.argv
tamanho_args = len(args)
print(args)
print(tamanho_args)

if tamanho_args <= 1:
    print("Voce não passou argumentos.")
else:
    print(f"Você passou os argumentos: {args[1:]}")
