# Gerenciador de Tarefas
# Objetivo: Objetivo:Criar um programa que permita ao usuário gerenciar suas tarefas diárias, usando operações de 
# listas para adicionar, remover e visualizar as tarefas.

def cadastro():
    gerenciador = {}

    lista_categorias = []


    while True:

        categoria = input("Cadastre uma categoria: ")
        lista_categorias.append(categoria.title())
        r = input("deseja cadastrar mais uma categoria? (S/N) ")
        if r.upper() in "N":
            break

    print()
    print("essas são as categorias cadastradas:")
    for item in lista_categorias:
        print("|",item, end=" | ")
        gerenciador[item] = []
    print()

    return (gerenciador,lista_categorias)

def adicionar(gerenciador, lista_categorias):
    print("Digite o nome da categoria para adicionar atividades: ")
    for item in lista_categorias:
        print("|",item, end=" | ")
    print()
    a = input()
      
    while True:
        tarefa = input("digite a tarefa: ")
        gerenciador[a.title()].append(tarefa.title())
        r = input("Deseja cadastrar mais uma tarefa? (S/N) ")
        if r.upper() in "N":
            break
    while True:
        r = input("Deseja adicionar atividades em outra categoria? (S/N) ")
        if r.upper() in "N":
            break
        else:
            print("Digite o nome da categoria para adicionar atividades: ")
            for item in lista_categorias:
                print("|",item, end=" | ")
            print()
            a = input()
            
            while True:
                tarefa = input("digite a tarefa: ")
                gerenciador[a.title()].append(tarefa.title())
                r = input("Deseja cadastrar mais uma tarefa? (S/N) ")
                if r.upper() in "N":
                    break
            
def remover(gerenciador,lista_categorias):
    print("Digite o nome da categoria para remover atividades: ")
    for item in lista_categorias:
        print("|",item, end=" | ")
    print()
    a = input()
    print(f"Atividades da categoria {a.title()}: ")
    for atvd in gerenciador[a.title()]:
        print("/",atvd, end=" / ")
    print()
    
    while True:
        tarefa = input("Digite a tarefa pra remover: ")
        gerenciador[a.title()].remove(tarefa.title())
        r = input("Deseja remover mais uma tarefa? (S/N) ")
        if r.upper() in "N":
            break

def visualizar(gerenciador, lista_categorias):  

    print("Essas são as suas categorias, qual você quer visualzar?")
    for item in lista_categorias:
        print("|",item, end=" | ")
    print()
    a = input()
    print("Essas são as atividades:")
    for atvd in gerenciador[a.title()]:
        print("-",atvd, end=" - ")
    print()

    return   

g, l = cadastro()

# Menu

while True:
    print()
    print("Escolha um opção: ")
    print("(1) Adicionar atividades.")
    print("(2) Remover atividades.")
    print("(3) Vizualizar atividades.")
    print("(4) Encerrar programa.")

    a = input()

    if a == "1":
        adicionar(g, l)
    elif a == "2":
        remover(g, l)
    elif a == "3":
        vizualizar(g, l)
    elif a == "4":
        break