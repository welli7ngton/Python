# Dada uma lista de dicionários com informações de alunos (nome, notas), crie uma nova lista 
# apenas com os nomes dos alunos que obtiveram média acima de 7 usando list comprehension.


alunos = [
    {"nome":"jose", "n1":7,"n2":6,"n3":9},
    {"nome":"maria", "n1":5,"n2":5,"n3":9},
    {"nome":"tiago", "n1":7,"n2":7,"n3":8},
    {"nome":"renan", "n1":8,"n2":7,"n3":7},
    {"nome":"jessica", "n1":7,"n2":5,"n3":9},
    {"nome":"mateus", "n1":8,"n2":8,"n3":9},
    {"nome":"savio", "n1":6,"n2":5,"n3":6}
]

aprovados = [
    aluno["nome"] 
    for aluno in alunos 
    if (aluno["n1"]+aluno["n2"]+aluno["n3"])/3 > 7
]

print(aprovados)