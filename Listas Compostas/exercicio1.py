# ler nome e peso de n pessoas
# guardar na lista
# mostrar:
# qtd cadastrada
# lista com pessoas mais pesadas
# lista com pessoas mais leves  

geral = []
dados = []

pesado = 0
leve = 0

while True:

    dados.append(str(input("nome: ")))
    dados.append(float(input("peso: ")))

    if len(geral) == 0:
        pesado = dados[1]
        leve = dados[1]

    else:
        if dados[1] > pesado:
            pesado = dados[1]
        if dados[1] < leve:
            leve = dados[1]

    geral.append(dados[:])
    
    dados.clear()

    r = input("deseja continuar? [S/N]")
    if r in "nN":
        break       

print("-=" *30)

print(f"o maior peso foi: {pesado}")

print(f"as pessoas mais pesadas são: ")

for p in geral:
    if p[1] == pesado:
        print(f"{p[0]}",end=", ")


print(f"o menor peso foi: {leve}")

print(f"as pessoas mais leve são:")   

for p in geral:
    if p[1] == leve:
        print(f"{p[0]}",end=", ")
