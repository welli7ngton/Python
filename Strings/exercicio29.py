#Construa um programa que leia duas strings fornecidas pelo usuario e verifique se a se- 
#gunda string lida esta contida no final da primeira, retornando o resultado da verificacao.

prim = input("digite uma string: ")
tamanhoprim = len(prim)

seg = input("digite a segunda string: ")
tamanhoseg = len(seg)

if tamanhoseg <= tamanhoprim:
    final = prim[tamanhoprim - tamanhoseg:]
    if final == seg:
        print(f"A string '{seg}' está contida no final da primeira string.")
    else:
        print(f"A string '{seg}' não está contida no final da primeira string.")
else:
    print("A segunda string é maior do que a primeira string.") 