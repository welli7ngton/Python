# Implemente um sistema de gerenciamento do salário de funcionários de uma empresa. Para isso, crie uma classe 
# Funcionario. Cada objeto dessa classe deve ter um nome e um salário. Faça os métodos setters para atribuir valores 
# para os atributos, assim como métodos getter que retornam esses métodos.

# Leve em consideração que o salário mínimo de um funcionário dessa empresa é 1000.0 reais e o máximo é 8000.0.


class Funcionario:

    def __init__(self):
        self.nome = None
        self.salario = None

    # getter
    @property
    def add_nome(self):       
        return self.nome

    # setter
    @add_nome.setter
    def add_nome(self,nome):
        self.nome = nome


    # getter
    @property
    def add_salario(self):
        return self.salario 

    # setter
    @add_salario.setter
    def add_salario(self,salario):
        self.salario = salario
      
        
wellington = Funcionario()
maria = Funcionario()
jose = Funcionario()

wellington.nome = "Wellington Almeida"
maria.salario = 7500.0

print(wellington.nome)

print(jose.nome)
jose.nome = "José Felipe"

maria.nome = "Maria Helena"

wellington.salario = 7000.0

jose.salario = 1000.0

print(wellington.nome)
print(wellington.salario)
print(maria.nome)
print(maria.salario)
print(jose.nome)
print(jose.salario)