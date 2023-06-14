
lista_tarefas = []
armazena_tarefas_excluidas = []

print("Ações:")
print("Desfazer, Refazer e Listar")
print("Digite Encerrar para finalizar a execução do programa.")
while True:
    acao = input("Digite uma tarefa ou uma ação: ").capitalize()
    if acao == "Desfazer":
        if lista_tarefas:
            tarefa = lista_tarefas.pop()
            armazena_tarefas_excluidas.append(tarefa)
        else:
            print("Não existe nenhuma tarefa para desfazer.")
            continue
    elif acao == "Refazer":
        if armazena_tarefas_excluidas:
            lista_tarefas.append(armazena_tarefas_excluidas[0])
            armazena_tarefas_excluidas.remove(armazena_tarefas_excluidas[0])
        else:
            print("Não existem tarefas para refazer.")
            continue
        
    elif acao == "Listar":
        if len(lista_tarefas) == 0:
            print("A lista está vazia.")
        else:
            for item in lista_tarefas:
                print(item)
    else:   
        lista_tarefas.append(acao)
    if acao.capitalize() == "Encerrar":
        break 
    