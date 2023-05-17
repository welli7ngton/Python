#Escreva um programa que recebe uma string S e inteiros nao-negativos I e J e imprima ˜
#o segmento S[I..J].

########################### o que está comentado é uma segunda forma de resolver ##################################

s = input("digite os dados da string S: ")

print("digite dois inteiros não negativos: ")
i = int(input())
j = int(input())

#intervaloij = ''

#if i > j:
    #maior = i
   # menor = j
#else:
 #   maior = j
 #   menor = i



#for a in range(menor,maior + 1):

    #intervaloij += s[a]

#print(f"os caracteres no intervalo I e J são: {intervaloij}")

print(s[i-1:j])
