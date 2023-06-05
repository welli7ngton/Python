# Exercício - sistema de perguntas e respostas
perguntas = [
    {
        'Pergunta': 'Quanto é 2+2?',
        'Opções': ['1', '3', '4', '5'],
        'Resposta': '4',
    },
    {
        'Pergunta': 'Quanto é 5*5?',
        'Opções': ['25', '55', '10', '51'],
        'Resposta': '25',
    },
    {
        'Pergunta': 'Quanto é 10/2?',
        'Opções': ['4', '5', '2', '1'],
        'Resposta': '5',
    },
]
pontuacao = 0
for dicionario in perguntas:
    for chave in dicionario:        
        if chave == "Resposta":
            break
        if chave == "Opções":
            
            for a in range(len(dicionario[chave])):
                print(f"{a}) {dicionario[chave][a]}")
                
        if chave == "Pergunta":
            print(dicionario[chave])
    r = int(input("Digite sua resposta: "))

    if dicionario["Opções"][r] == dicionario["Resposta"]:
        pontuacao += 1
        print("Resposta correta!")
    else:
        print("Resposta incorreta")
print(f"Sua pontuação foi {pontuacao} de 3.")