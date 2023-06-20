# Intro
# Seu sistema deverá:

# Inicializar.
# Iniciar de tanque vazio, sem ninguém dentro e com 0 de quilometragem.
# Para simplificar, nosso carro esportivo suporta até 2 pessoas e seu tanque suporta até 100 litros de água como combustível.

# Entrando e Saindo.
# Embarcar uma pessoa por vez.
# Desembarcar uma pessoa por vez.
# Não embarque além do limite ou desembarque se não houver ninguém no carro.

# Abastecer.
# Abastecer o tanque passando a quantidade de litros de combustível.
# Caso tente abastecer acima do limite, descarte o valor que passou.

# Dirigir.
# Caso haja pelo menos uma pessoa no carro e algum combustível, ele deve gastar combustível andando e aumentar a quilometragem.
# Nosso carro faz um kilômetro por litro de água.
# Caso não exista combustível suficiente para completar a viagem inteira, dirija o que for possível e emita uma mensagem indicando quanto foi percorrido.


class Carro:

    def __init__(self):
        self.quilometragem = 0
        self.combustivel = 0.0
        self.passageiros = 0
    
    def embarque(self):
        if self.passageiros == 2:
            print("Capacidade máxima atingida.")
            return False
        self.passageiros += 1

    def desembarque(self):
        if self.passageiros == 0:
            print("Ninguém para desembarcar.")
            return False
        self.passageiros -= 1

    def abastecer(self):
        if self.combustivel == 100:
            print("Tanque cheio.")
            return False
        abastecimento = float(input("Digite a quantidade que quer abastecer em litros."))

        self.combustivel += abastecimento
        if self.combustivel > 100:
            self.combustivel -= (self.combustivel-100)

    def dirigir(self):
        if self.passageiros == 0:
            print("O carro não pode andar sem ao menos um passageiro.") 
            return False
        if self.combustivel == 0:
            print("O carro não pode andar sem combustível, abasteça para prosseguir.")
            return False
        
        viagem = float(input("Digite a quantidade de km's da viagem: "))
        if viagem > self.combustivel:
            self.quilometragem += self.combustivel
            print(f"Combustível acabou, {self.combustivel}km's percorridos")
            self.combustivel = 0
            return True
        
        self.combustivel -= viagem
        self.quilometragem += viagem
