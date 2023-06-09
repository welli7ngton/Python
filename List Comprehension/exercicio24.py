# Dada uma lista de dicionários com informações de produtos (nome, preço), crie uma 
# nova lista apenas com os nomes dos produtos cujo preço esteja entre 100 e 200 
# usando list comprehension.


produtos = [
    {"nome":"p1","preco":125.00},
    {"nome":"p2","preco":80.00},
    {"nome":"p3","preco":300.00},
    {"nome":"p4","preco":199.00},
    {"nome":"p5","preco":10.00},
    {"nome":"p6","preco":101.00},
    {"nome":"p7","preco":201.00},
    {"nome":"p8","preco":95.00},
    {"nome":"p9","preco":190.00}
]

nl = [
    (prod["nome"],prod["preco"]) 
    for prod in produtos
    if prod["preco"] >= 100.00 and prod["preco"] <= 200.00
]

print(nl)