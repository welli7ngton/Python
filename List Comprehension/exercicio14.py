# Dada uma lista de dicionários com informações de produtos (nome, preço), crie uma nova 
# lista apenas com os nomes dos produtos cujo preço seja menor que 50 usando list 
# comprehension.


produtos = [
    {"nome":"p1", "preco":49.99},
    {"nome":"p2", "preco":7.00},
    {"nome":"p3", "preco":55.00},
    {"nome":"p4", "preco":51.00},
    {"nome":"p5", "preco":10.00},
    {"nome":"p6", "preco":15.00},
    {"nome":"p7", "preco":27.00},
    {"nome":"p8", "preco":50.00},
    {"nome":"p9", "preco":99.00},
    {"nome":"p10", "preco":50.00},
    {"nome":"p20", "preco":1.00},
    {"nome":"p21", "preco":48.00},
    {"nome":"p30", "preco":98.00},
    {"nome":"p31", "preco":70.00}
]


nova_lista = [produto["nome"] for produto in produtos if produto["preco"] < 50.00]

print(nova_lista)