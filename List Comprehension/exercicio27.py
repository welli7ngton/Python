# Dada uma lista de dicionários com informações de alunos (nome, notas), crie uma 
# nova lista  com os nomes dos alunos que obtiveram a média 10 e uma lista com os 
# alunos que não obtiveram a média 6 usando list comprehension.


alunos = [
    {"nome":"Wellington","nota1":10,"nota2":10},
    {"nome":"Pedro","nota1":7,"nota2":6},
    {"nome":"Maria","nota1":5,"nota2":5},
    {"nome":"Isa","nota1":2,"nota2":7},
    {"nome":"Renan","nota1":7,"nota2":4},
    {"nome":"Tiago","nota1":9,"nota2":10},
    {"nome":"Renata","nota1":4,"nota2":7},
    {"nome":"Rian","nota1":10,"nota2":10},
    {"nome":"Marcia","nota1":10,"nota2":5},
    {"nome":"Fernanda","nota1":7,"nota2":7},
    {"nome":"Olga","nota1":3,"nota2":6},
    {"nome":"Mel","nota1":1,"nota2":9},
]

med_10 = [
    aluno["nome"]
    for aluno in alunos
    if aluno["nota1"] == 10 and aluno["nota2"] == 10
]


med_6 = [
    aluno["nome"]
    for aluno in alunos
    if (aluno["nota1"] + aluno["nota2"])/2 < 6
]

print("Alunos com média 10.")
print(med_10)
print("Alunos com média abaixo de 6")
print(med_6)