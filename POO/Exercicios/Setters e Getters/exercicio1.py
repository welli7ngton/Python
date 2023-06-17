# 1- Crie uma classe chamada "Person" com as propriedades name e age. Implemente um getter para age que retorna a idade 
# da pessoa em meses.


class Person:

    def __init__(self,nome,idade):
        self.nome = nome
        self.idade = idade
    
    def get_idade(self):
        return self.idade * 12


p1 = Person("joao", 20)

idade_em_meses = p1.get_idade()

print(idade_em_meses)