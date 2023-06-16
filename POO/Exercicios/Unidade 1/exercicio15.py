# 5- Crie uma classe chamada "Agenda" que permite adicionar eventos em datas 
# específicas e listar os eventos de um determinado dia.

class Agenda:

    def __init__(self,nome):
        
        self.nome = nome
        self.agenda = {}
        print(f"Agenda de {self.nome}")
    
    def add_evento(self):
        print(self.nome)
        data = input("Digite a data para salvar o evento: ")
        evento = input("Digite o evento: ")
        self.agenda[data] = evento

    def listar_todos_eventos(self):
        for data,evento in self.agenda.items():
            print(f"\tData: {data} | Evento: {evento}")
    
    def lista_evento_especifico(self):
        data = input("Digite a data do evento para listar: ")
        if data not in self.agenda:
            print("Data sem eventos.")
            return
        
        print(f"Evento: {self.agenda[data]}")

a1 = Agenda("Wellington")

a1.add_evento()
a1.add_evento()

a1.listar_todos_eventos()

a2 = Agenda("Maria")
a1.add_evento()
a2.add_evento()
a1.lista_evento_especifico()
a2.add_evento()
a2.listar_todos_eventos()

