# 9- Crie uma classe chamada "Estudante" com atributos de instância "nome" e 
# "curso" e um método "apresentar_estudante" que imprime o nome e o curso do 
# estudante.

class Estudante:

    def __init__(self,nome,curso):
        self.nome = nome.title()
        self.curso = curso.title()

    def apresentar_estudante(self):
        print(self.nome)
        print(self.curso)

a1 = Estudante("wellington almeida","redes de computadores")

a1.apresentar_estudante()