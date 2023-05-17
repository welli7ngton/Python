#O codigo de Cesar e uma das mais simples e conhecidas tecnicas de criptografia.  E um 
#tipo de substituicao na qual cada letra do texto  e substituıda por outra, que se apresenta
#no alfabeto abaixo dela um numero fixo de vezes. Por exemplo, com uma troca de tres
#posicoes, ‘A’ seria substituıdo por ‘D’, ‘B’ se tornaria ‘E’, e assim por diante. Implemente
#um programa que faca uso desse Codigo de Cesar (3 posicoes), entre com uma string e 
#retorne a string codificada. Exemplo:
#String: a ligeira raposa marrom saltou sobre o cachorro cansado
#Nova string: D OLJHLUD UDSRVD PDUURP VDOWRX VREUH R FDFKRUUR FDQVDGR


s = str(input("digite a mensagem que deseja codificar: "))
novafrase = ''

for letra in s:

    cod = ord(letra) + 3
    novafrase += chr(cod)

novafrase = novafrase.replace('#', ' ')
    



print(f"a nova frase é: {novafrase.upper()}")
