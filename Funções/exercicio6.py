#5- Faça um programa com uma função chamada somaImposto. A função possui dois parâmetros formais:
# taxaImposto, que é a quantia de imposto sobre vendas expressa em porcentagem e custo, que é o custo
# de um item antes do imposto. A função “altera” o valor de custo para incluir o imposto sobre vendas.


def somaImposto(taxaImposto, custo):
    taxa = taxaImposto / 100
    valor = custo * (1 + taxa)
    return valor

taxa = float(input("Digite a taxa de imposto: "))
custo = float(input("Digite o custo: "))

valor_com_imposto = somaImposto(taxa, custo)

print(f"O valor com imposto é: {valor_com_imposto:.2f}")

