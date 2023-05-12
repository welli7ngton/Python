from exercicio3 import alunos_redes

c = 0

medias = []
alunos = []

while True:
    a1 = alunos_redes()

    r = a1.verifica_aprovacao()
    medias.append(r)
    if r >= 6.0:
        print("apovrado")

    else:
        print("reprovado")
    
    c += 1  
    if c == 5:
        break

mai, men, nmai, nmen = a1.verifica_medias(medias)

print(f"a maior media foi de {nmai}: {mai}")
print(f"a menor media foi de {nmen}: {men}")

