soma = 0
qtd = 0

for a in range(0, 501):
    if a %3 == 0 and a %2 != 0:
        soma += a
        qtd += 1
print(f"a soma dos {qtd} numeros resulta em {soma}")