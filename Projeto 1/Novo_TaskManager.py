# Gerenciador de Tarefas
# Objetivo: Objetivo:Criar um programa que permita ao usuário gerenciar suas tarefas diárias, usando operações de 
# listas para adicionar, remover, editar e visualizar as tarefas.

def adicionar(gerenciador, lista_categorias):
    for item in lista_categorias:
        print("|",item, end=" | ")
    print()
    a = input("Digite o nome da categoria para adicionar atividades: ")
    
    
    while True:
        tarefa = input("digite a tarefa: ")
        gerenciador[a.title()].append(tarefa.title())
        r = input("deseja cadastrar mais uma tarefa? (S/N) ")
        if r.upper() in "N":
            break
    while True:
        r = input("deseja adicionar atividades em outra categoria? (S/N) ")
        if r.upper() in "N":
            break
        else:
            for item in lista_categorias:
                print("|",item, end=" | ")
            print()
            a = input("Digite o nome da categoria para adicionar atividades: ")
            
            while True:
                tarefa = input("digite a tarefa: ")
                gerenciador[a].append(tarefa.title())
                r = input("deseja cadastrar mais uma tarefa? (S/N) ")
                if r.upper() in "N":
                    break
            



gerenciador = {}
data_hora = {}
lista_categorias = []
status = None

while True:

    categoria = input("Cadastre uma categoria: ")
    lista_categorias.append(categoria.title())
    r = input("deseja cadastrar mais uma categoria? (S/N) ")
    if r.upper() in "N":
        break

print("essas são as categorias cadastradas:")
for item in lista_categorias:
    print("|",item, end=" | ")
    gerenciador[item] = []
print()
adicionar(gerenciador, lista_categorias)

print(gerenciador)
