# 3- Crie uma classe chamada "Pessoa" com atributos de instância "nome" e 
# "endereço" e um método "adicionar_telefone" que permite adicionar um telefone à 
# lista de telefones da pessoa.

class Pessoa:

    def __init__(self,nome,endereco):
        self.nome = nome.title()
        self.endereco = endereco.title()
        self.lista_tel = {}
    
    def adicionar_telefone(self):
        nome = input("Digite o nome do contato: ").title()
        
        if nome in self.lista_tel:
            print("Nome ja existe na lista, para não ocorrer erros adicione um nome diferente ao contato.")
            nome = input("Digite o nome do contato: ").title()
            tel = input("Digite o telefone para adicionar:")
            self.lista_tel[nome] = tel
            return True
        tel = input("Digite o telefone para adicionar:")
        self.lista_tel[nome] = tel
        print("Contato salvo.")
        

    def listar_telefones(self):
        for nome,tel in self.lista_tel.items():
            print(f"\tNome:{nome} \n \tContato:{tel}")

p1 = Pessoa("Wellington","Rua1")

p1.adicionar_telefone()
p1.adicionar_telefone()
p1.listar_telefones()
p1.adicionar_telefone()
p1.listar_telefones()