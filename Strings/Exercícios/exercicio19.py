#Fac¸a um programa em que troque todas as ocorrencias de uma letra L1 pela letra L2 em ˆ
#uma string. A string e as letras L1 e L2 devem ser fornecidas pelo usuario. 


frase = input("digite uma frase: ")

l1 = input("digite L1: ")
l2 = input("digite l2: ")
novafrase = ''
for letra in frase:

    if letra == l1:
        novafrase += l2
    else:
        novafrase += letra

print(novafrase)


