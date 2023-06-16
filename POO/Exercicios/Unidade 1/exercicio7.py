# 7- Crie uma classe chamada "Livro" com atributos de instância "título", "autor" e "ano" e um método "detalhes" que 
# imprime todas as informações do livro.

class Livro:

    def __init__(self, titulo, autor, ano):
        self.titulo = titulo
        self.autor = autor
        self.ano = ano
    
    def detalhes(self):
        print(self.titulo)
        print(self.autor)
        print(self.ano)


l1 = Livro("Matemática","Escola",2002)

l1.detalhes()