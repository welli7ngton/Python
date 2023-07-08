# Exercício 7: Agendador de tarefas
# Crie uma classe chamada AgendadorTarefas que permita agendar tarefas para
# datas e horários específicos. A classe deve fornecer métodos para adicionar
# tarefas, listar as tarefas agendadas e executar as tarefas que estão no
# momento agendado.

from datetime import datetime


class AgendadorTarefas:

    def __init__(self, nome) -> None:
        self.nome = nome
        self.tarefas = {}

    def add_tarefa(self, tarefa, data, hora):
        data_ = datetime.strptime(data + " " + hora,  "%d/%m/%Y %H:%M")
        self.tarefas[data_] = tarefa

    def listar_tarefas(self):
        print(f"\nAgenda de {self.nome}\n")
        for data, tarefa in self.tarefas.items():
            print(f"Data: {data} | Tarefa: {tarefa}")

    def executa_tarefa(self):
        hora_atual = datetime.now().time()
        print(f"{hora_atual}")


if __name__ == "__main__":
    a1 = AgendadorTarefas("Wellington")

    a1.add_tarefa("Correr", "8/7/2023", "18:00")
    a1.add_tarefa("Jogar", "8/7/2023", "20:00")
    a1.add_tarefa("Passear", "8/7/2023", "17:00")
    a1.add_tarefa("Estudar", "8/7/2023", "14:00")
    a1.add_tarefa("Trabalhar", "8/7/2023", "09:00")
    a1.add_tarefa("Acordar", "8/7/2023", "08:00")
    a1.listar_tarefas()
