# Crie uma classe abstrata chamada ContaBancaria com métodos abstratos depositar() e sacar(). Implemente classes 
# concretas para representar diferentes tipos de conta bancária, como conta corrente e conta poupança. Cada classe deve 
# fornecer uma implementação adequada dos métodos abstratos.

import random

class ContaBancaria:

    def depositar(self,valor_deposito):
        pass

    def sacar(self,valor_saque):
        pass

    def transferencia(self, valor_transferencia,conta_beneficiado):
        pass

class ContaCorrente(ContaBancaria):

    def __init__(self,nome,conta):
        self.nome = nome
        self.conta = conta
        self.saldo = 0.0
        self.juros = 0
        self.log = []

    def depositar(self,valor_deposito):
        if valor_deposito <= 0:
            print("Operação de depósito inválida.")
            self.log.append("Depósito falho.")
            return False
        print("Conta onde será depositado:",self.conta)
        print("Titular:",self.nome)
        self.saldo += valor_deposito
        print("Operação realizada com sucesso.")
        self.log.append("Depósito.")
        return True
    
    def sacar(self,valor_saque):
        if  valor_saque > self.saldo:
            print("Saldo insuficiente, operação inválida.")
            self.log.append("Saque falho.")
            return False
        
        self.saldo -= valor_saque
        print("Operação realizada com sucesso.")
        self.log.append("Saque.")
        return True

    def verificar_saldo(self):
        print("Saldo atual:",self.saldo)
        self.log.append("Verificação de saldo.")

    def transferencia(self, valor_transferencia,conta_beneficiado):
        if valor_transferencia > self.saldo:
            print("Saldo insuficiente, Operação inválida.")
            self.log.append("Transferẽncia falha.")
            return False
        print(f"O valor de {valor_transferencia} será transferido para conta bancária :{conta_beneficiado}.")
        self.saldo -= valor_transferencia
        print("Operação realizada.")
        self.log.append("Transferẽncia.")
        return True

    def extrato(self):
        self.log.append("Verificação de extrato.")
        print()
        print("EXTRATO")
        for extrato in self.log:
            print("Ação:",extrato)
        print()  

class ContaPolpanca(ContaBancaria):

    def __init__(self,nome,conta):
        self.nome = nome
        self.conta = conta
        self.saldo = 0.0
        self.possui_cartao_debito = False
        self.saldo_cheque = 1000
        self.num_cartao = None

    def depositar(self,valor_deposito):
        if valor_deposito <= 0:
            print("Operação de depósito inválida.")
            return False
        print("Conta onde será depositado:",self.conta)
        print("Titular:",self.nome)
        self.saldo += valor_deposito
        print("Operação de Depósito realizada com sucesso.")
        return True
    
    def sacar(self,valor_saque):
        if  valor_saque > self.saldo:
            print("Saldo insuficiente, operação inválida.")
            return False
        self.saldo -= valor_saque
        print("Operação de Saque realizada com sucesso.")
        return True

    def transferencia(self, valor_transferencia,conta_beneficiado):
        if valor_transferencia > self.saldo:
            print("Saldo insuficiente, Operação inválida.")
            return False
        print(f"O valor de {valor_transferencia} será transferido para conta bancária :{conta_beneficiado}.")
        self.saldo -= valor_transferencia
        print("Operação de Transferência realizada.")
        return True

    def cheque(self,valor_cheque):
        if valor_cheque > self.saldo:
            print("Saldo insuficiente, operação inválida.")
            return False
        if self.saldo_cheque < valor_cheque:
            print("Saldo para gerar cheque insuficiente, solicite mais saldo ou espere até que mais saldo seja liberado.")
            return False   

        self.saldo_cheque -= valor_cheque
        self.saldo -= valor_cheque
        print("Operação de Cheque realizada com sucesso.")
        return True

    def pagamento(self,conta,valor):
        if valor > self.saldo:
            print("Operação inválida, saldo insuficiente.")
            return False
        
        self.saldo -= valor
        print(f"Conta {conta} foi paga no valorde {valor}.")
        return True

    def verificar_saldo(self):
        print("Saldo atual:",self.saldo)
    
    def gera_cartao(self):
        if self.possui_cartao_debito:
            print("Você não pode obter um novo cartão de débito.")
            return False
        self.possui_cartao_debito = True
        self.num_cartao = random.randint(100000000,999999999)
        print("O número do seu cartão é:",self.num_cartao)
        return True

c1 = ContaCorrente("Wellington",123)
c2 = ContaPolpanca("Wellington",123)

print()
c1.depositar(1000)
c1.verificar_saldo()
c1.sacar(50)
c1.extrato()
c1.transferencia(550,234)
c1.verificar_saldo()
c1.extrato()
print()
c2.depositar(1000)
c2.verificar_saldo()
c2.sacar(50)
c2.transferencia(550,234)
c2.cheque(200)
c2.pagamento("agua",75.00)
c2.verificar_saldo()
c2.gera_cartao()
c2.gera_cartao()
