# Crie uma classe abstrata chamada Produto com métodos abstratos calcular_preco() e exibir_detalhes(). Implemente 
# classes concretas para representar diferentes tipos de produtos, como livro, eletrônico e vestuário. Cada classe deve 
# fornecer uma implementação adequada dos métodos abstratos.

class Produto:

    def calcular_preco(self,preco,imposto):
        ...
    
    def exibir_detalhes(self):
        ...

class Papelaria(Produto):
    def __init__(self,nome,quantidade):
        self.nome = nome
        self.quantidade =  quantidade
    
    def calcular_preco(self,preco,imposto=15):
        self.preco = preco
        self.imposto = imposto
        self.categoria = __class__.__name__

        print(f"Preço sem imposto({self.nome}): R${self.preco}, imposto: {self.imposto}% por unidade, preco com imposto para categoria {self.categoria}: R${self.preco + (self.preco*(imposto/100))}")
        print(f"Valor total do estoque: R${(self.preco + (self.preco*(imposto/100)))*self.quantidade}")

    def exibir_detalhes(self):
        print()
        print(f"Informaçoes da Classe {__class__.__name__}:")
        print(f"Nome Produto: {self.nome}")
        print(f"Quantidade: {self.quantidade}")
        print(f"Preço sem impostos: R${self.preco}")
        print(f"Imposto: {self.imposto}%")
        print()

class Eletronicos(Produto):
    def __init__(self,nome,quantidade):
        self.nome = nome
        self.quantidade =  quantidade
    
    def calcular_preco(self,preco,imposto=None):
        self.preco = preco
        self.imposto = "Sem imposto"
        self.categoria = __class__.__name__

        print(f"Preço sem imposto({self.nome}): R${self.preco}, imposto: {self.imposto}, preco com imposto para categoria {self.categoria}: R${self.preco}")
        print(f"Valor total do estoque: R${(self.preco *self.quantidade)}")

    def exibir_detalhes(self):
        print()
        print(f"Informaçoes da Classe {__class__.__name__}:")
        print(f"Nome Produto: {self.nome}")
        print(f"Quantidade: {self.quantidade}")
        print(f"Preço sem impostos: R${self.preco}")
        print(f"Imposto: sem impostos no estado para este tipo de produto.")
        print()

class Vestuario(Produto):
    def __init__(self,nome,quantidade):
        self.nome = nome
        self.quantidade =  quantidade
    
    def calcular_preco(self,preco,imposto=15):
        self.preco = preco
        self.imposto = imposto - 6
        self.categoria = __class__.__name__

        print(f"Preço sem imposto({self.nome}): R${self.preco}, imposto: {self.imposto}% por unidade, preco com imposto para categoria {self.categoria}: R${self.preco + (self.preco*(imposto/100)):.2f}")
        print(f"Valor total do estoque: R${((self.preco + (self.preco*(imposto/100)))*self.quantidade):.2f}")

    def exibir_detalhes(self):
        print()
        print(f"Informaçoes da Classe {__class__.__name__}:")
        print(f"Nome Produto: {self.nome}")
        print(f"Quantidade: {self.quantidade}")
        print(f"Preço sem impostos: R${self.preco}")
        print(f"Imposto: {self.imposto}%(imposto reduzido em 6%).")
        print()

livro = Papelaria("Harry Potter",15)
celular = Eletronicos("Iphone 11",12)
calca = Vestuario("Calça jeans",25)

livro.calcular_preco(170.00)
print()
celular.calcular_preco(3200)
print()
calca.calcular_preco(100)

livro.exibir_detalhes()
celular.exibir_detalhes()
calca.exibir_detalhes()