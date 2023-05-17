#Faca um programa para ler uma tabela contendo os nomes dos alunos de uma turma de
#5 alunos. O programa deve solicitar ao usuario os nomes do aluno, sempre perguntando 
#se ele deseja inserir mais um nome na lista. Uma vez lidos todos os alunos, o usuario 
#ira indicar um nome que ele deseja verificar se esta presente na lista, onde o programa 
#deve procurar pelo nome (ou parte deste nome) e se encontrar deve exibir na tela o nome
#completo e o indice do vetor onde esta guardado este nome. 

alunos : [str] = [0 for x in range(5)]

for a in range(0, 5):
    alunos[a] = input("digite o nome do aluno: ")

    sn = input("deseja adicionar mais um aluno(S/N)? ")

    if sn in "nN":
        break
print("######################################")
nome = input("digite o nome que quer procurar: ")
indice = int(input("digite onde quer porcurar: "))

if indice <= len(alunos):
    if nome in alunos[indice]:
        print(f"o aluno encontrado foi: {alunos[indice]}")
    else:
        print("o aluno não foi encontrado. ")
else:
    print("o indice digitado é maior que a quantidade de alunos cadastrados.")

    