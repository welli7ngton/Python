palavra = "teste"
letra_acertada = ""



while True:
    letra = input("digite uma letra: ")
    
    if len(letra) > 1:
        print("digite apenas uma letra.")
        continue
    
    if letra in palavra:
        letra_acertada += letra
    
    palavra_formada = ""
    for letra_s in palavra:
        if letra_s in letra_acertada:
            palavra_formada += letra_s
        else:
            palavra_formada += "_"

    if palavra_formada == palavra:
        print("voce ganhou")
        break
        
        
  