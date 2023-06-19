# 7- Crie uma classe chamada "Funcionário" com atributos de instância "nome" e "cargo" e um método "apresentar_cargo" 
# que imprime o nome e o cargo do funcionário.

class Funcionario:

    def __init__(self, nome,cargo):
        self.nome = nome
        self.cargo = cargo

    def apresentar_cargo(self):
        print("Nome:",self.nome,"\nCargo:",self.cargo)


f1 = Funcionario("Wellington","Estagiario")
f1.apresentar_cargo()

f2 = Funcionario("Maria","Dev")
f2.apresentar_cargo()