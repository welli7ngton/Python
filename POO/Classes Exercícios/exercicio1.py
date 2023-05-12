#1. Crie uma classe que modele uma pessoa
#(a) Atributos: nome, idade e endereco
#(b) Metodos: mostrar endereco e alterar endereco 


class Pessoa:

    def __init__(self, nome, idade, endereco):
        self.nome = nome
        self.idade = idade
        self.endereco = endereco
        return

    def muda_endereco(self):
        novo_endereco = input("digite seu novo endereço: ")
        self.endereco = novo_endereco
        
        return


