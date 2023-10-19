testes = int(input("digite a quantidade de testes: "))

qtdc = 0
qtdr = 0
qtds = 0

for a in range(0, testes):

    qtd = int(input("digite a quantidade de cobaias: "))
    tipo = input("digite o tipo da cobaia: ")

    if tipo == "C" or tipo == "c":
        qtdc += qtd
    elif tipo == "R" or tipo == "r":
        qtdr += qtd
    else:
        qtds += qtd

qtdtotal = qtdc + qtdr + qtds

print("RELATORIO FINAL: ")
print(" ")
print(f"total de cobaias: {qtdtotal}")
print(f"quantidade de coelhos: {qtdc}")
print(f"quantidade ratos: {qtdr}")
print(f"quantidade sapos: {qtds}")
print(" ")

totalf = float(qtdtotal)

pc = float(qtdc)
pr = float(qtdr)
ps = float(qtds)

porcc = (pc * 100)/ totalf
porcr = (pr * 100)/ totalf
porcs = (ps * 100)/ totalf

print(f"percentual de coelhos: {porcc:.2f}")
print(f"percentual de ratos: {porcr:.2f}")
print(f"percentual de sapos: {porcs:.2f}")
