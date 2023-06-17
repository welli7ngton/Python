# Exercicio Baralho OBI
# https://olimpiada.ic.unicamp.br/pratique/ps/2021/f1/baralho/

dados = input()

P = [0 for x in range(13)]
U = [0 for x in range(13)]
C = [0 for x in range(13)]
E = [0 for x in range(13)]


for a in range(0,len(dados),3):
    conjunto = dados[a:a+3]
    for i in range(0,len(conjunto)):
        num = conjunto[:2]
        numint = int(num)
        naipe = conjunto[2]

    if naipe == "P":
        if num in P:
            P[numint -1] = 14
        else:
            P[numint-1] = num

    elif naipe == "U":
        if num in U:
            U[numint -1] = 14
        else:
            U[numint-1] = num 

    elif naipe == "E":
        if num in E:
            E[numint -1] = 14
        else:
            E[numint-1] = num

    elif naipe == "C":
        if num in C:
            C[numint -1] = 14
        else:
            C[numint-1] = num
zerop = 0
if 14 in P:
    P = "erro"
else:
    for verifica_0 in range(0,len(P)):
        if P[verifica_0] == 0:
            zerop += 1

qtdp = 13 - zerop
faltaP = 13 - qtdp

verifica_0 = 0
zerou = 0
if 14 in U:
    U = "erro"
else:
    for verifica_0 in range(0,len(U)):
        if U[verifica_0] == 0:
            zerou += 1

qtdu = 13 - zerou
faltaU = 13 - qtdu


verifica_0 = 0
zeroc = 0
if 14 in C:
    C = "erro"
else:
    for verifica_0 in range(0,len(C)):
        if C[verifica_0] == 0:
            zeroc += 1
qtdc = 13 - zeroc
faltaC = 13 - qtdc


verifica_0 = 0
zeroe = 0
if 14 in E:
    E = "erro"
else:
    for verifica_0 in range(0,len(E)):
        if E[verifica_0] == 0:
            zeroe += 1
qtde = 13 - zeroe
faltaE = 13 - qtde


if faltaC == 0:
    print("erro")
else:
    print(faltaC)

if faltaE == 0:
    print("erro")
else:
    print(faltaE)

if faltaU == 0:
    print("erro")
else:
    print(faltaU)

if faltaP == 0:
    print("erro")
else:
    print(faltaP)