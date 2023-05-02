tabuleiro = []
l = '1'
cont = 0
for i in range(8):
    linha = [l for i in range(8)]
    tabuleiro.append(linha)
    
    linha += str(cont)
    cont += 1 

'''for a in range(8):'''
for b in range(8):
    print(tabuleiro[b])


    