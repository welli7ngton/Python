# Quadrado mágico. Um quadrado mágico é aquele dividido em linhas e colunas, com um número em cada posição
# e no qual a soma das linhas, colunas e diagonais é a mesma. Por exemplo, veja um quadrado mágico de lado 3
# com números de 1 a 9:
#	    8  3  4 
#	    1  5  9
#	    6  7  2
# Elabore uma função que identifica e se o quadrado digitado é um quadrado magico ou não.



def testequadrado(vetorsomas):

    for a in range(len(vetorsomas)):
        if vetorsomas[a] == somateste:
            verificacao = True
        else:
            verificacao = False
            break
    return(verificacao)
    
soma : [int] = [0 for x in range(8)]

qm : [int] = [0 for x in range(9)]

for a in range(9):
    qm[a] = int(input("digite cada valor do quadrado mágico:"))
    
print()
print("seu quadrado mágico é: ")
print(qm[:3])
print(qm[3:6])
print(qm[6:])
print()

somateste = sum(qm[:3])

# soma das linhas
c1 = qm[0] + qm[1] + qm[2]
soma[0] = c1
c2 = qm[3] + qm[4] + qm[5]
soma[1] = c2
c3 = qm[6] + qm[7] + qm[8]
soma[2] = c3


# soma das diagonais
c4 = qm[0] + qm[4] + qm[8]
soma[3] = c4
c5 = qm[2] + qm[4] + qm[6]
soma[4] = c5

# soma das colunas
c6 = qm[0] + qm[3] + qm[6]
soma[5] = c6
c7 = qm[1] + qm[4] + qm[7]
soma[6] = c7
c8 = qm[2] + qm[5] + qm[8]
soma[7] = c8

r = testequadrado(soma)

if r == True:
    print("É um quadrado mágico.")

else:
    print("Não é um quadrado mágico.")
