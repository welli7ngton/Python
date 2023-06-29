# Herança simples - Relações entre classes
# Associação - usa, Agregação - tem, Composição - é dono de, Herança -  é um
# 
# Classe principal (ex: Pessoa)
#   -> super class, base class ou parent class
# Classes filhas (ex: Cliente)
#   -> sub class, child class, derived class 

# super class | classe principal | generica
class Pessoa:
    def __init__(self, nome, sobrenome):
        self.nome = nome
        self.sobrenome = sobrenome

    def falar_nome_classe(self):
        print("Nome:",self.nome,self.sobrenome,"\nClasse:",self.__class__.__name__)

# sub class | classe filha | especializada
class Cliente(Pessoa):
    ...

# sub class | classe filha | especializada 
class Aluno(Pessoa):
    ...

c1 = Cliente("Wellington", "Almeida")
c1.falar_nome_classe()
a1 = Aluno("Maria", "Helena")
a1.falar_nome_classe()
