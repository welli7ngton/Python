'''
Implemente um programa que irá calcular a média dos alunos de um turma com n alunos, com o valor de n informado pelo usuário.

O programa irá receber a nota da AP1 dos alunos e  depois a nota da AP2 dos alunos. O programa irá calcular e imprime a média desses n alunos.

ATENÇÃO: É obrigatório usar três listas.

Três professor?

Isso três.

Três???.

Exatamente três.

Duas listas para armazenar as notas das APs, cada lista representando uma AP, e a terceira para armazenar a média dos alunos.  

Entrada:

6

2.5 6.0 8.0 5.2 9.8 4.0                       

3.5 6.0 7.0 6.8 7.2 6.0

Saída:

3.00 6.00 7.50 6.00 8.50 5.00
'''

alunos = int(input())

ap1 = [0 for x in range(alunos)]
ap2 = [0 for x in range(alunos)]
medias = [0 for x in range(alunos)]

for a in range(0, alunos):
    ap1[a] = float(input())

for a in range(0, alunos):
    ap2[a] = float(input())
    
for a in range(alunos):
    medias[a] = (ap1[a] + ap2[a]) /2
    num = ("{:.2f}".format(medias[a]))
    medias[a] = num

print("{}".format(medias))