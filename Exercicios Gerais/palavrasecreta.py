palavra = "teste"
p = ""
for letra in palavra:
    p += "_"

print(p)
while True:
    letra = input("digite uma letra: ")
    
    if letra in palavra:
        for a in range(len(palavra)):
            if palavra[a] == letra:
                print(p[a].replace("_", letra))
                
                break
    