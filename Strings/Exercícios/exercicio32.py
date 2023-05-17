#Faca um programa que contenha um menu com as seguintes opcoes: 
#(a) Ler uma string S1 (tamanho maximo 20 caracteres); 
#(b) Imprimir o tamanho da string S1;
#(c) Comparar a string S1 com uma nova string S2 fornecida pelo usuario e imprimir o 
#resultado da comparacao; 
#(d) Concatenar a string S1 com uma nova string S2 e imprimir na tela o resultado da
#concatenacao; 
#(e) Imprimir a string S1 de forma reversa;
#(f) Contar quantas vezes um dado caractere aparece na string S1. Esse caractere
#desse ser informado pelo usuario; 
#(g) Substituir a primeira ocorrencia do caractere C1 da string S1 pelo caractere C2. Os 
#caracteres C1 e C2 serao lidos pelo usuario; 
#(h) Verificar se uma string S2 e substring de S1. A string S2 deve ser informada pelo 
#usuario; 
#(i) Retornar uma substring da string S1. Para isso o usuario deve informar a partir de 
#qual posicao deve ser criada a substring e qual  e o tamanho da substring. 

print("##########    MENU    ##########")
print("Opção(a):Ler uma string S1 (tamanho maximo 20 caracteres)")
print("Opção(b):Imprimir o tamanho da string S1")
print("Opção(c):Comparar a string S1 com uma nova string S2 fornecida pelo usuario e imprimir o resultado da comparacao")
print("Opção(d):Concatenar a string S1 com uma nova string S2 e imprimir na tela o resultado da concatenacao")
print("Opção(e):Imprimir a string S1 de forma reversa")
print("Opção(f):Contar quantas vezes um dado caractere aparece na string S1. Esse caracteredesse ser informado pelo usuario")
print("Opção(g):Substituir a primeira ocorrencia do caractere C1 da string S1 pelo caractere C2. Os caracteres C1 e C2 serao lidos pelo usuario")
print("Opção(h):Verificar se uma string S2 e substring de S1. A string S2 deve ser informada pelo usuario")
print("Opção(i):Retornar uma substring da string S1. Para isso o usuario deve informar a partir de qual posicao deve ser criada a substring e qual  e o tamanho da substring. ")
print("################################")

print()
cont = 0
opcao = input("digite uma opção: ")

if opcao in 'aA':
    s1 = input("digite a string com tamanho maximo de 20 caracteres: ")
    if len(s1) > 20:
        print("erro.")
    else:
        print(f"o tamanho da string {s1} é : {len(s1)}.")

elif opcao in 'bB':
    s1 = input("digite s1: ")
    print(f"o tamanho de s1 é: {len(s1)}")

elif opcao in "cC":
    s1 = input("digite s1: ")
    s2 = input("digite s2: ")

    if s2 == s1:
        print("s1 é igual s2")
    else:
        print("s1 é doferente de s2")

elif opcao in "dD":
    s1 = input("digite s1:")
    s2 = input("digite s2:")
    s3 = s1 + s2
    print(f"a concatenação de '{s1} e '{s2}'   é igual a {s3}")

elif opcao in "eE":
    s1 = input("digite s1: " ) 
    print(f"o inverso de '{s1}' é: {s1[::-1]}")  

elif opcao in "fF":
    s1 = input("digite s1: ")
    c = input("digite o caractere: ")
    print(f"o caractere {c} aparece {s1.count(c)} vezes em {s1}")

elif opcao in "gG":
    s1 = input("digite s1: ")
    c1 = input("digite C1: ")
    c2 = input("digite C2: ")

    print(s1.replace(c1, c2))
elif opcao in "hH":
    s1 = input("digite s1: ")
    s2 = input("digite s2: ")

    if s2 in s1:
        print("s2 é uma substring de s1")
    else:
        print("s2 não é uma subtring de s2")

elif opcao in "iI":
    s2 = input("digite s1: ")
    ini = int(input("digtie onde deve começar a substring: "))
    tamanho = int(input("digite o tamanho da substring: "))    
    sub = s2[ini:ini + tamanho]
    print (sub)