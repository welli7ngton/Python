# Dada uma lista de dicionários com informações de pessoas (nome, idade, sexo), crie uma 
# nova lista apenas com as pessoas do sexo feminino usando list comprehension.


pessoas = [
    {"nome": "Maria", "idade": 25, "sexo": "Feminino"},
    {"nome": "João", "idade": 30, "sexo": "Masculino"},
    {"nome": "Ana", "idade": 22, "sexo": "Feminino"},
    {"nome": "Pedro", "idade": 27, "sexo": "Masculino"},
    {"nome": "Carla", "idade": 35, "sexo": "Feminino"},
    {"nome": "Lucas", "idade": 28, "sexo": "Masculino"},
    {"nome": "Dávila", "idade": 19, "sexo": "Feminino"}
]


l = [p for p in pessoas if "Feminino" in p["sexo"]]

for i in l:
    print(i)
