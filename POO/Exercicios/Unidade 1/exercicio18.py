# 8- Crie uma classe chamada "Jogo" com métodos "iniciar", "jogar" e "encerrar" que representam as etapas de um jogo.


class Jogo:

    __perguntas = ["Quanto é 5+5?","Quanto é 5x5","Quanto é 25/5","Quanto é 100-(5x5)?"]
    __respostas = [10,25,5,75]
    

    def __init__(self,nome):
        self.nome = nome
        self.pontuacao = 0
        self.respostas_jogador = []
        print("O jogo iniciou...")


    def fazer_pergunta(self):
        for i in range(len(Jogo.__perguntas)):
            print(Jogo.__perguntas[i])
            r = int(input())
            self.respostas_jogador.append(r)
    
    def verifica_resposta(self):
        for i in range(len(Jogo.__respostas)):
            if self.respostas_jogador[i] == Jogo.__respostas[i]:
                self.pontuacao += 15
            else:
                self.pontuacao -= 5

    def mostra_pontuacao(self):
        print("Jogador:",self.nome,"\nPontuação:",self.pontuacao,"pts")


j1 = Jogo("Wellington")
j1.fazer_pergunta()
j1.verifica_resposta()
j1.mostra_pontuacao()