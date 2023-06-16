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


p1 = Pessoa("Wellington",20,"Morada Nova","88 9 8176-2299","wellingtonasilva45@gmail.com")

p2 = Pessoa("José",32,"Pau dos Ferros", "85 9 8734-7728","jose1234@outlook.com")

expo = [p1.__dict__,p2.__dict__]

with open("__dados.json","w",encoding="utf-8") as arq:
    json.dump(expo,arq,indent=2)