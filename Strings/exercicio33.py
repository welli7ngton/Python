#Leia uma cadeia de caracteres no formato “DD/MM/AAAA” e copie o dia, mes e ano para 
#3 variaveis inteiras. Antes disso, verifique se as barras estao no lugar certo, e se DD, MM 
#e AAAA sao numericos.



cadeia = input("digite a cadeia: ")

if cadeia[2] == "/" and cadeia[5] == "/":
    for a in range(0, len(cadeia)):
        if ord(cadeia[a]) > 47 and ord(cadeia[a]) < 92 or cadeia[a] == "/":
            print("testando segundo pedido...")
        else:
            print("a cadeia não atende o segundo pedido")
            break

else:
    print("a cadeia nao atende ao primeiro pedido")

dia = int(cadeia[:2])
mes = int(cadeia[3:5])
ano = int(cadeia[6:9+1])

print(f"dia {dia}, mes {mes}, ano {ano}")

#DD / MM / AAAA
#01 2 34 5 6789