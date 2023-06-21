# Crie uma classe abstrata chamada Funcionario com métodos abstratos calcular_salario() e exibir_informacoes(). ]
# Implemente classes concretas para representar diferentes tipos de funcionários, como gerente, vendedor e estagiário. 
# Cada classe deve fornecer uma implementação adequada dos métodos abstratos.


class Funcionario:
    
    def exibir_salario(self,dias_trabalhados):
        ...

    def exibir_informacoes(self):
        ...


class Gerente(Funcionario):
    
    def __init__(self,nome,idade,funcao,salario_base,bonus=16):
        self.nome = nome
        self.idade = idade
        self.funcao = funcao
        self.salario_base = salario_base + (salario_base*(bonus/100))

    def exibir_salario(self,dias_trabalhados):
        diaria = self.salario_base/26
        salario = diaria * dias_trabalhados
        
        print(f"O salario de {self.nome} pelos dias trabalhados com o bônus aplicado é: {salario:.2f}")

    def exibir_informacoes(self):
        print("Informações Gerente:")
        print(f"Nome: {self.nome}")
        print(f"Idade: {self.idade}")
        print(f"Função: {self.funcao}")

class Vendedor(Funcionario):

    def __init__(self,nome,idade,funcao,salario_base,bonus=13):
        self.nome = nome
        self.idade = idade
        self.funcao = funcao
        self.salario_base = salario_base + (salario_base*(bonus/100))
    
    def exibir_salario(self,dias_trabalhados):
        diaria =  self.salario_base/24
        salario = diaria*dias_trabalhados
        print(f"O salario de {self.nome} pelos dias trabalhados com o bônus aplicado é: {salario:.2f}")

    def exibir_informacoes(self):
        print("Informações Vendedor:")
        print(f"Nome: {self.nome}")
        print(f"Idade: {self.idade}")
        print(f"Função: {self.funcao}")  

class Estagiario(Funcionario):

    def __init__(self,nome,idade,funcao,salario_base,bonus=5):
        self.nome = nome
        self.idade = idade
        self.funcao = funcao
        self.salario_base = salario_base + (salario_base*(bonus/100))

    def exibir_salario(self,dias_trabalhados):
        diaria =  self.salario_base/18
        salario = diaria*dias_trabalhados
        print(f"O salario de {self.nome} pelos dias trabalhados com o bônus aplicado é: {salario:.2f}")

    def exibir_informacoes(self):
        print("Informações Estagiário:")
        print(f"Nome: {self.nome}")
        print(f"Idade: {self.idade}")
        print(f"Função: {self.funcao}")  


josue = Gerente("Josué Fernandes",33,"Gerenciar lojas",1735.0)
marina = Vendedor("Marina Medeiros",25,"Vender e atender",1220.0)
wellington = Estagiario("Wellington Almeida",20,"Informática",730.0)

josue.exibir_salario(26)
marina.exibir_salario(24)
wellington.exibir_salario(18)

print()
josue.exibir_informacoes()
print()
marina.exibir_informacoes()
print()
wellington.exibir_informacoes()