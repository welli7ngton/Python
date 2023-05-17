#Escreva um programa que leia duas palavras e diga qual deles vem primeiro na ordem
#alfabetica. ´ Dica: ‘a’ e menor do que ‘b’.

p1 = input("digite a primeira palavra: ")

p2 = input("digite a segunda palavra: ")


pos = 0



qtd1 = len(p1)
qtd2 = len(p2)

if qtd1 > qtd2:
    maior = qtd1
    menor = qtd2
else:
    maior = qtd2
    menor = qtd1

 
if p1 == p2:
    print("as palavras são iguais")


for a in range(menor):

    if p1[pos] == p2[pos]:
        pos += 1
    else:

        if p1[pos] < p2[pos]:
            print(f"{p1} vem primeiro na ordem alfabetica")
            break
        else:
            print(f"{p2} vem primeiro na ordem alfabetica") 
            break      