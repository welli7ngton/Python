# Crie uma classe chamada "Funcionário" com atributos de instância "nome", 
# "salário" e "departamento" e um método "transferir_departamento" que transfere 
# o funcionário para um novo departamento.


class Funcionario:

    def __init__(self,nome,salario,departamento):
        self.nome = nome
        self.salario = salario
        self.departamento = departamento

    
    def altera_departamento(self):
        self.departamento = input("Digite o novo departamento: ")

    def dados_funcioario(self):
        print("Nome:",self.nome)
        print("Salário:",self.salario)
        print("Departamento:",self.departamento)
        
f1 = Funcionario("Wellington",1100,"TI")
f1.dados_funcioario()
f1.altera_departamento()
f1.dados_funcioario()
