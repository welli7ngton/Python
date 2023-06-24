# Budega

# Nosso objetivo no trabalho é modelar uma fila de atendimento de um Mercatil.

# Intro
# Quando o mercantil é incializado, é definido a quantidade de caixas que ele terá.

# Os caixas são modelados como um vetor de clientes de tamanho fixo. Uma posição do caixa ou terá o valor null para indicar que o caixa está vazio ou terá um objeto cliente.

# A fila de espera é uma lista de clientes de tamanho variável. Todo cliente que chega é inserido no final da fila.

# As operações são entrar, chamarNoCaixa e finalizarAtendimento.


import time

class Budega:

    def __init__(self):

        self.caixa1 = []
        self.caixa2 = []
        self.caixa3 = []
        self.caixa_rapido1 = []
        self.caixa_rapido2 = []

        self.lista_caixas = [
            self.caixa1,
            self.caixa2,
            self.caixa3
            ]

        self.caixas_rapidos = [
            self.caixa_rapido1,
            self.caixa_rapido2
            ]

    def verifica_filas(self):
        pos = 1
        for i in self.lista_caixas:
            print(f"\nCaixa {pos}\n")
            for j in i:
                print(f"\t{j.nome}") 
            pos += 1  

        pos = 1
        for i in self.caixas_rapidos:
            print(f"\nCaixa Rápido {pos}\n")
            for j in i:
                print(f"\t{j.nome}") 
            pos += 1 

    def chamar_no_caixa(self,caixa_pos):
        try:
            caixa = self.lista_caixas[caixa_pos -1]
        except IndexError:
            print("O caixa não existe.")
            return False
        for pessoa in caixa:
            print(f"{pessoa.nome} está em atendimento.\n")
            pessoa.status_atendimento = True
            time.sleep(2)
            print(f"cliente atendido.\n")
            caixa.pop(caixa.index(pessoa))
            time.sleep(1)
            return True
    
    def chamar_no_caixa_rapido(self,caixa_pos):
        try:
            caixa = self.lista_caixas[caixa_pos -1]
        except IndexError:
            print("O caixa não existe.")
            return False
        for pessoa in caixa:
            print(f"{pessoa.nome} está em atendimento.\n")
            pessoa.status_atendimento = True
            time.sleep(2)
            print(f"cliente atendido.\n")
            caixa.pop(caixa.index(pessoa))
            time.sleep(1)
            return True


        

class Cliente:

    def __init__(self,nome,qtd_itens,idade):
        self.nome = nome
        self.qtd_itens = qtd_itens
        self.prioridade = True if idade > 60 else False
        self.status_atendimento = False
    
    def entra_fila(self,other):
        
        if self.prioridade or self.qtd_itens <= 15:
            tamanho_filas = [len(item) for item in other.caixas_rapidos]
            for caixa in other.caixas_rapidos:
                if len(caixa) ==  min(tamanho_filas):
                    caixa.append(self)
                    print(f"O cliente {self.nome} entrou na fila.")
                    return True
        else:
            tamanho_filas = [len(item) for item in other.lista_caixas]

            for caixa in other.lista_caixas:
                if len(caixa) == min(tamanho_filas):
                    caixa.append(self)
                    print(f"O cliente {self.nome} entrou na fila.")
                    return True


b1 = Budega()
c1 = Cliente("Wellington",14,20)
c2 = Cliente("Jose",20,70)
c3 = Cliente("Raimunda",20,70)
c5 = Cliente("Rian",20,20)
c4 = Cliente("Helena",20,20)
c6 = Cliente("Maria",20,20)


c1.entra_fila(b1)
c2.entra_fila(b1)
c3.entra_fila(b1)
c4.entra_fila(b1)
c5.entra_fila(b1)
c6.entra_fila(b1)
b1.verifica_filas()
b1.chamar_no_caixa(4)
b1.chamar_no_caixa(1)
b1.verifica_filas()
