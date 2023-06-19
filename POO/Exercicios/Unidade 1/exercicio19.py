# Crie uma classe chamada "Loja" que permite adicionar produtos ao estoque, realizar vendas e calcular o valor total das vendas.

class Loja:
    estoque = {}
    total_vendas = 0.0
    def add_prod(self,produto,quantidade,valor):
        Loja.estoque[produto] = quantidade
        Loja.total_vendas -= valor
    def venda(self,produto,qtd_venda,valor_produto):
        Loja.total_vendas += qtd_venda * valor_produto
        Loja.estoque[produto] = Loja.estoque[produto] - qtd_venda

    def mostra_venda(self):
        print("Lucro líquido:",Loja.total_vendas)

    def mostra_estoque(self):
        print("="*15,"Estoque","="*15)
        for produto,qtd in Loja.estoque.items():
            print("Produto:",produto,"\nQuantidade:",qtd)
        print("="*38)
l1 = Loja()

l1.add_prod("Feijão 1kg",60,4.45)
l1.add_prod("Arroz 1kg",60,3.49)
l1.add_prod("Macarão 500g",60,2.99)

l1.mostra_estoque()

l1.venda("Feijão 1kg",20,5.79)
l1.mostra_estoque()
l1.mostra_venda()