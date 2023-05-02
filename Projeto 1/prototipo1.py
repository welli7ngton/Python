# Gerenciador de Tarefas
# Objetivo: Objetivo:Criar um programa que permita ao usuário gerenciar suas tarefas diárias, usando operações de listas para adicionar, remover, editar e visualizar as tarefas.


# Criação da lista de categorias

print("############### CRIAÇÃO ###############")
print()

tamanho_categorias = int(input("Quantas categorias você irá cadastrar? "))
print(f"    A sua lista poderá amrazenar {tamanho_categorias} categorias.")

categorias = []

for a in range(0, tamanho_categorias):
    categorias += "0"

print()

print("Digite quais categorias você quer adicionar.")

nomes_categorias = ''

for a in range(0, len(categorias)):
    nomes_categorias = input()
    categorias[a] = nomes_categorias

print(f"    Estas são as suas categorias de atividade: {categorias}")

print()
print("#######################################")

# Definindo as tarefas por categoria

print()

titulos_categorias = categorias

print(f"Escolha um ìndice de 1 à {tamanho_categorias} para começar a adicionar as tarefas em cada categoria.")
for a in range(0, tamanho_categorias):
    print(f"{a + 1} = {titulos_categorias[a]}")

selecao = int(input())
selecao -= 1


print()
print("Agora vamos começar a distribuir as atividades.")
atividades = []

# Definindo o tamanho de atividades #######
for a in range(0, 10):                    #
    atividades += ' '                     #
   #print(len(atividades))                #
###########################################


print("Você terá 10 espaços para armazenar suas atividades em cada categoria.")
print("digite a atividade e prazo para conclusão no tipo (atividade/mes|dia.)")
print("    Exemplo: correr/jan|07")
for a in range(0, 10):
    atividades[a] += input("digite a atividade:")
    opcao = int(input("digite '1' para adicionar mais uma atividade ou '2' para encerrar."))
    if opcao == 2:
        break
    

tupla1 = (titulos_categorias[selecao],atividades)
print(tupla1)

tuplageral = tupla1

print(tuplageral)











print()
print("############################################################################")