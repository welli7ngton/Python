from exercicio2 import aluno

a1 = aluno("wellington", 100, "redes")
print("deseja alterar curso? (S/N)")
r = input()
if r.upper() == "S":

    a1.altera_curso("poo")