# Crie uma classe para representar um jogador de futebol, com os atributos nome, posição, data de nascimento, 
# nacionalidade, altura e peso. Crie os métodos públicos necessários para sets e gets e também um método para imprimir 
# todos os dados do jogador. Crie um método para calcular a idade do jogador e outro método para mostrar quanto tempo 
# falta para o jogador se aposentar. Para isso, considere que os jogadores da posição de defesa se aposentam em média 
# aos 40 anos, os jogadores de meio-campo aos 38 e os atacantes aos 35.

class jogador:

    def __init__(self,nome,posicao,data_nascimento,nacionalidade,altura,peso):
        self.nome = nome
        self.posicao = posicao
        self.data_nascimento = data_nascimento
        self.nacionalidade = nacionalidade
        self.altura = altura
        self.peso = peso

    def calcula_idade(self):
        ano_atual = 2023
        ano_nasc = self.data_nascimento[6:]
        self.idade = ano_atual - int(ano_nasc)
        return self.idade
    
    def aposentadoria(self):
        if self.posicao.lower() == "defesa":
            return f"Faltam {40 - self.idade} anos para a aposentadoria."

        elif self.posicao.lower() == "meio-campo":
            return f"Faltam {38 - self.idade} anos para a aposentadoria."

        elif self.posicao.lower() == "ataque":
            return f"Faltam {35 - self.idade} anos para a aposentadoria"

        elif self.posicao not in ["defesa","meio-campo","ataque"]:
            print("Posição inválida")
            return False
    
j1 = jogador("Wellington","meio-campo","07/12/2002","Brasileiro",1.83,65.0)

j1.calcula_idade()
print(j1.aposentadoria())

