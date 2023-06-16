# 1- Crie uma classe chamada "CarrinhoDeCompras" que permite adicionar itens ao 
# carrinho e calcular o valor total da compra.

class CarrinhoDeCompras:

    def __init__(self,carrinho=[],valor_compra=0.0):
        self.carrinho = carrinho 
        self.valor_compra = valor_compra

    
    def adicionar(self,item,valor_item):
        self.carrinho.append(item.capitalize())
        self.valor_compra += valor_item
        print(item.capitalize(),"foi adicionado no carrinho.")

    def calcular(self):
        print(f"O valor total da compra é:R${self.valor_compra}")

    def listar_carrinho(self):
        print("Carrinho:")
        for item in self.carrinho:
            print(f"\t{item}")

c1 = CarrinhoDeCompras()

c1.adicionar("chocolate",10.99)

c1.calcular()
c1.adicionar("maçã kg",4.25)
c1.adicionar("laranja kg",1.79)
c1.calcular()
c1.adicionar("leite",15.99)

c1.calcular()
c1.listar_carrinho()

