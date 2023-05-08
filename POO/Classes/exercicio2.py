#2. Crie uma classe que modele uma aluno
#(a) Atributos: nome, numero de matrıcula e curso
#(b) Metodos: mostrar curso e alterar curso


class aluno:

    def __init__(self, nome, matricula, curso):
        self.nome = nome
        self.matricula = matricula
        self.curso = curso
        print(f"{nome}, {matricula}, {curso}")
        return

    def altera_curso(self, novocurso):
        self.curso = novocurso
        print(f"{self.nome}, {self.matricula}, {self.curso}")