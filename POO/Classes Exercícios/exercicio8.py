#8. Crie uma classe que modele uma conta corrente
#(a) Atributos: numero da conta, nome do correntista e saldo 
#(b) Metodos: alterar nome, deposito e saque; No construtor, saldo  é opcional, com valor 
#default zero e os demais atributos sao obrigatorios.



class conta:

    def __init__(self, numero_conta,nome, saldo=1000):

        self.numero_conta = int(numero_conta)
        self.nome = nome
        self.saldo = float(saldo)


    def mostrainfo(self):
        print(f"conta: {self.numero_conta}")
        print(f"titular: {self.nome}")
        print(f"saldo atual: {self.saldo}")   
    
    def alteranome(self):

        self.nome = input("digite o novo nome: ")

    
    def deposito(self):

        print(f"conta: {self.numero_conta}")
        print(f"titular: {self.nome}")
        print(f"saldo atual: {self.saldo}")
        dep = float(input("digite o valor de depósito: "))
        self.saldo += dep
        print(f"novo saldo: {self.saldo}")

    
    def saque(self):

        print(f"conta: {self.numero_conta}")
        print(f"titular: {self.nome}")
        print(f"saldo atual: {self.saldo}")
        if self.saldo == 0:
            print("saldo zerado, impossivel realizar operação.")
        else:
            saq = float(input("digite o valor do saque: "))
            if saq > self.saldo:
                print("operação inválida.")
            else:
                self.saldo -= saq
                print(f"novo saldo: {self.saldo}")
