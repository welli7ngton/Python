obj = int(input("Você deseja Codificar(1) ou Decodificar(2)? "))

if obj == 1:
    chave = int(input("Qual a chave de Codificação? "))
    print("Digite a mensagem para codificar: ")
    mensagem = input()
    novamensagem =''
    novaletra = ''

    for letra in mensagem:
        nvalorascii = ord(letra) + chave
        novaletra = chr(nvalorascii)
        novamensagem += novaletra
    
    print("a nova mensagem é: ")
    print(novamensagem[::-1])

elif obj == 2:
    chave = int(input("Digite a chave para Decodificar: "))
    print("Digite a mensagem para Decodificar: ")
    mensagem = input()
    antigamensagem = ''
    for letra in mensagem:
        avalorascii = ord(letra) - chave
        antigaletra = chr(avalorascii)
        antigamensagem += antigaletra
    
    print("a mensagem decodificada é: ")
    print(antigamensagem[::-1])
