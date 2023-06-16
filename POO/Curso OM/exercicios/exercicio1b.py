# Exercício - Salve sua classe em JSON
# Salve os dados da sua classe em JSON
# e depois crie novamente as instâncias
# da classe com os dados salvos
# Faça em arquivos separados.
from exercicio1a import Pessoa
import json



with open("__dados.json","r",encoding="utf-8") as arq:
    impor = json.load(arq)

p1 = Pessoa(**impor[0])
p2 = Pessoa(**impor[1])

print(p1.nome)
print(p2.nome)