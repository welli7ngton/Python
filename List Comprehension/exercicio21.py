# Dada uma lista de dicionários com informações de funcionários (nome, salário), crie uma nova lista apenas com os 
# nomes dos funcionários que têm salário acima da média usando list comprehension.

funcionarios = [
    {"nome":"Wellington","salario":5500.00},
    {"nome":"Rian","salario":10000.00},
    {"nome":"Maria","salario":7500.00},
    {"nome":"Joao","salario":4000.00},
    {"nome":"Pedro","salario":5000.00},
    {"nome":"Melisa","salario":2200.00},
    {"nome":"Renata","salario":7050.00},
    {"nome":"Ricardo","salario":1100.00},
    {"nome":"Aquila","salario":4000.00},
    {"nome":"Tiago","salario":3200.00},
    {"nome":"Marcio","salario":1600.00},
    {"nome":"Ronne","salario":2300.00},
]

media_salario = 0
for i in funcionarios:
    media_salario += i["salario"]

media_salario /= len(funcionarios)

nl = [
    (funcionario["nome"],funcionario["salario"])
    for funcionario in funcionarios
    if funcionario["salario"] > media_salario
]

print(media_salario)
print(nl)