# 3- Crie uma classe chamada "Pessoa" com atributos de instância "nome" e "idade" e um método "dizer_oi" que imprime 
# uma saudação com o nome da pessoa.

class Pessoa:

    def __init__(self,nome,idade):
        self.nome = nome.capitalize()
        self.idade = idade
    
    def dizer_oi(self):
        return f"Olá, {self.nome} como vai?"

p1 = Pessoa("wellington",20)

print(p1.dizer_oi())

p2 = Pessoa("maria",18)

print(p2.dizer_oi())

p3 = Pessoa("João",23)

print(p3.dizer_oi())