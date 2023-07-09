# 6- Escreva um script que crie uma estrutura de diretórios específica
# com base em uma lista de nomes de pastas fornecida pelo usuário.

import os

HOME = os.path.expanduser("~")
HOME += os.path.join("/Desktop")


def cria_pasta(nomepasta_: str):
    os.makedirs(HOME+"/"+nomepasta_, exist_ok=True)
    print("Pasta criada.")
    return True


def cria_subpasta(nomepasta_: str, subpasta_: str):
    if os.path.isdir(HOME+"/"+nomepasta_):
        os.makedirs(HOME+"/"+nomepasta_+"/"+subpasta_, exist_ok=True)
        print("Subpasta criada.")
        return True
    print("Não foi possível criar subpasta.")
    return False


while True:

    print("\nDigite '1' para criar pasta")
    print("Digite '2' para criar subpasta")
    print("Digite '3' para listar as pastas disponívels")
    print("Digite '0' para sair\n")

    r = input("Digite uma ação: ")

    if r == "1":
        cria_pasta(input("Digite o nome da pasta: "))

    elif r == "2":
        nome = input("Digite o nome da pasta: ")
        sub = input("Digite o nome da subpasta: ")
        cria_subpasta(nome, sub)

    elif r == "3":
        for root, dirs, files in os.walk(HOME):
            print(root)
            # print(dirs)
    elif r == "0":
        break
