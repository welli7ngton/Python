# Dada uma lista de dicionários com informações de alunos (nome, notas), crie uma nova lista apenas com os nomes 
# dos alunos que tiraram notas acima da média da turma usando list comprehension.


alunos = [
    {"nome":"wellington","nota1":8,"nota2":9},
    {"nome":"jose","nota1":5,"nota2":9},
    {"nome":"pedro","nota1":7,"nota2":7},
    {"nome":"rian","nota1":8,"nota2":8},
    {"nome":"maria","nota1":7,"nota2":8},
    {"nome":"jessica","nota1":5,"nota2":7},
    {"nome":"aline","nota1":4,"nota2":7},
    {"nome":"joao","nota1":6,"nota2":7},
    {"nome":"renan","nota1":6,"nota2":6},
    {"nome":"tiago","nota1":3,"nota2":5},
    {"nome":"igor","nota1":2,"nota2":4},
    {"nome":"marilia","nota1":6,"nota2":5}
]

media = 0
for i in alunos:
    media += (i["nota1"] + i["nota2"])/2

media /= len(alunos)






acima_media_turma = [
    (aluno["nome"], (aluno["nota1"]+aluno["nota2"])/2)
    for aluno in alunos 
    if (aluno["nota1"] + aluno["nota2"])/ 2 > media
]

print(acima_media_turma)