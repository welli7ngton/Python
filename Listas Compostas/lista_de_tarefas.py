
lista_tarefas = []
armazena_tarefas_excluidas = []

print("Ações:")
print("Desfazer, Refazer e Listar")
while True:
    acao = input("Digite uma tarefa ou uma ação: ").capitalize()
    if acao == "Desfazer":
        try:
            armazena_tarefas_excluidas.append(lista_tarefas[len(lista_tarefas) - 1])
            lista_tarefas.pop()
        except IndexError:
            print("Não é possível excluir um item de uma lista vazia.")
            continue
    elif acao == "Refazer":
        try:
            lista_tarefas.append(armazena_tarefas_excluidas[len(armazena_tarefas_excluidas) - 1])
        except IndexError:
            print("Não há nada para refazer.")
            continue
    elif acao == "Listar":
        if len(lista_tarefas) == 0:
            print("A lista está vazia.")
        else:
            for item in lista_tarefas:
                print(item)
    else:   
        lista_tarefas.append(acao)