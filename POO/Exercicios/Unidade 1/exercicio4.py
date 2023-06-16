# 4- Crie uma classe chamada "ContaBancária" com atributos de instância "titular" e "saldo" e métodos para depositar 
# e sacar dinheiro da conta.


class ContaBancaria:
    
    def __init__(self,titular):
        self.titular = titular
        self.saldo = 0
    
    def verifica_saldo(self):
        print(f"Seu saldo atual é: {self.saldo}")
        return True
    
    def deposito(self):
        novo_deposito = float(input("Digite o valor a ser depositado:"))

        self.saldo += novo_deposito
        print(f"O novo saldo é: {self.saldo}")

    def saque(self,valor_para_saque):
        if self.saldo <= 0 or valor_para_saque > self.saldo:
            print("Operação indisponível, saldo insuficiente")
            return

        self.saldo -= valor_para_saque
        print("Operação realizada.")
        print(f"Novo saldo: {self.saldo}")
        return f"R$ {valor_para_saque}"
    

conta1 = ContaBancaria("Wellington")

conta1.verifica_saldo()
conta1.deposito()
conta1.verifica_saldo()
conta1.saque(10000)