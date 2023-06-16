# Exercício - Salve sua classe em JSON
# Salve os dados da sua classe em JSON
# e depois crie novamente as instâncias
# da classe com os dados salvos
# Faça em arquivos separados.

import json

class Pessoa:

    def __init__(self,nome,idade,cidade,telefone,email):
        self.nome = nome
        self.idade = idade
        self.cidade = cidade
        self.telefone = telefone
        self.email = email
dados = [1,2,3]
with open("__dados.json","r",encoding="utf-8") as arq:
    dados = json.load(arq)


p1 = Pessoa(**dados)

print(p1.nome)
print(p1.idade)
print(p1.cidade)
print(p1.telefone)
print(p1.email)