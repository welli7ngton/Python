# 5- Crie uma classe chamada "Student" com as propriedades name e grades. Implemente um getter para grades que retorna 
# uma string formatada com todas as notas do aluno.

class Student:

    def __init__(self,nome, notas):
        self.nome = nome
        self.notas = notas

    def get_notas_formatadas(self):
        notas_formatadas = ", ".join(str(nota) for nota in self.notas)
        return f"Nome do Aluno: {self.nome} | Notas: {notas_formatadas}"

    def get_media(self):
        self.media = sum(self.notas)/len(self.notas)
        return f"Média de {self.nome}: {self.media}"




a1 = Student("Wellington",[8.0,9.5,7.2,9.3])
a2 = Student("Rian",[9.0,9.5,9.2,9.1])
a3 = Student("Pedro",[8.5,9.5,6.2,9.0])

print(a1.get_notas_formatadas())
print(a2.get_notas_formatadas())
print(a3.get_notas_formatadas())

print(a1.get_media())
print(a2.get_media())
print(a3.get_media())


