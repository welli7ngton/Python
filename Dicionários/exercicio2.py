# copy, sorted, produtos.sort
# Exercícios

from copy import deepcopy

def gera_novos_produtos(produtos):
    # Aumente os preços dos produtos a seguir em 10%
    # Gere novos_produtos por deep copy (cópia profunda)
    
    novos_produtos = deepcopy(produtos)
    for produto in novos_produtos:
        produto["preco"] +=  round(produto["preco"] * 0.1, 2)

    print("Produtos:")
    print(*produtos,sep="\n")
    print()
    print("Produtos com novos preços:")
    print(*novos_produtos,sep="\n")

    return True

def ordena_produtos_dec(produtos):
    # Ordene os produtos por nome decrescente (do maior para menor)
    # Gere produtos_ordenados_por_nome por deep copy (cópia profunda)
    
    produtos_ordenados_por_nome = sorted(
        produtos,
        key=lambda p:p["nome"],
        reverse=True
        )
    print("Produtos:")
    print(*produtos,sep="\n")
    print()
    print("Produtos ordenados em decrescente:")
    print(*produtos_ordenados_por_nome,sep="\n")    

    return True

def ordena_preco(produtos):
    # Ordene os produtos por preco crescente (do menor para maior)
    # Gere produtos_ordenados_por_preco por deep copy (cópia profunda)
    produtos_ordenados_por_preco = sorted(
        produtos,
        key=lambda preco: preco["preco"]
    )

    print("Produtos:")
    print(*produtos,sep="\n")
    print()
    print("Produtos ordenados por preços:")
    print(*produtos_ordenados_por_preco,sep="\n")

    return

produtos = [
    {'nome': 'Produto 5', 'preco': 10.00},
    {'nome': 'Produto 1', 'preco': 22.32},
    {'nome': 'Produto 3', 'preco': 10.11},
    {'nome': 'Produto 2', 'preco': 105.87},
    {'nome': 'Produto 4', 'preco': 69.90}
]

# Exercicio 1
gera_novos_produtos(produtos)
print()
# Exercicio 2
ordena_produtos_dec(produtos)
print()
# Exercicio 3
ordena_preco(produtos)