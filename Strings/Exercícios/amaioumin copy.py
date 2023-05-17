'''
Entre com um nome e imprima o nome somente se a primeira letra do nome for “a”
(maiuscula ou min  uscula).
'''


nome = input("digite um nome: ")

if nome[0] == 'a' or nome[0] == 'A':
    print(nome)
else:
    print("não começa com 'a ou 'A' ")