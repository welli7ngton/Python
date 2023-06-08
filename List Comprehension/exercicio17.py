# Dada uma lista de dicionários com informações de livros (título, autor, ano), crie uma 
# nova lista apenas com os títulos dos livros cujo ano seja maior que 2000 usando list 
# comprehension.

livros = [
    {"titulo":"livro1","autor":"wellington", "ano": 2001},
    {"titulo":"livro2","autor":"wellington", "ano": 1000},
    {"titulo":"livro3","autor":"wellington", "ano": 2022},
    {"titulo":"livro4","autor":"wellington", "ano": 200},
    {"titulo":"livro5","autor":"wellington", "ano": 1999},
    {"titulo":"livro6","autor":"wellington", "ano": 2000},
    {"titulo":"livro7","autor":"wellington", "ano": 2000},
    {"titulo":"livro8","autor":"wellington", "ano": 2034},
    {"titulo":"livro9","autor":"wellington", "ano": 2000},
    {"titulo":"livro0","autor":"wellington", "ano": 3000},
    {"titulo":"livro10","autor":"wellington", "ano": 2003},
]


nl = [
    livro["titulo"]
    for livro in livros 
    if livro["ano"] > 2000
]

print(nl)