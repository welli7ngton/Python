# 4- Crie uma classe chamada "Funcionário" com atributos de instância "nome" e 
# "salário" e um método "aumentar_salário" que aumenta o salário do funcionário em 
# uma determinada porcentagem.

class Funcionario:

    def __init__(self,nome,salario):
        self.nome = nome.title()
        self.salario = salario

    def aumentar_salario(self,porcentagem):
        self.salario += self.salario * (porcentagem/100)
        print(f"Salário de {self.nome} aumentado.")

    def mostrar_salario(self):
        print(f"Salário atual: {self.salario}")   

s1 = Funcionario("wellingto almeida",5500)     
s1.mostrar_salario()
s2 = Funcionario("Rian", 10000)
s2.mostrar_salario()

s1.aumentar_salario(15)
s2.aumentar_salario(10)
s1.mostrar_salario();s2.mostrar_salario()