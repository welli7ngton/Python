# 2- Crie uma classe chamada "Banco" que permite cadastrar clientes, abrir contas 
# bancárias e fazer transferências entre contas.
import random
saldos = {}
class Banco: 

    def __init__(self,nome,idade,email):
        global saldos
        self.nome = nome
        self.idade = idade
        self.email = email
        self.conta = random.randint(100,999)
        self.saldo = 0.0
        self.senha = None
        saldos[self.conta] = self.saldo

    def cadastro(self):
        global saldos
        self.saldo = saldos[self.conta]
        print("Informações do cadastro:")
        print("Nome:",self.nome)
        print("Idade:",self.idade)
        print("Conta:",self.conta)
        if self.senha == None:
            self.senha = int(input("Digite a sua senha numérica de 4 dígitos: "))
        r = input("Deseja ver seu saldo? (Y/N)")
        if r in "Yy":
            print()
            print("Saldo:",self.saldo)
            print()

    def deposito(self,valor_deposito):
        global saldos
        self.saldo += valor_deposito
        print("Depósido realizado com sucesso.")
        saldos[self.conta] = self.saldo
        
    def saque(self,valor_saque):
        global saldos
        if self.saldo == 0 or valor_saque > self.saldo:
            print("Operação inválida, saldo insuficiente.")
            return False
        self.saldo -= valor_saque
        print("Operação realizada com sucesso.")
        saldos[self.conta] = self.saldo
        return True
    
    def transferencia(self, valor_transferencia):
        conta = int(input("Digite a conta que receberá a transferência: "))
        global saldos
        if valor_transferencia > self.saldo:
            print("Operação inválida, saldo insuficiente.")
            return False

        senha = int(input("Digite sua senha para completar a acção: "))
        if senha != self.senha:
            print("Senha inválida, Finalizando operação...")
            return False

        self.saldo -= valor_transferencia
        transferencia =  saldos[conta] + valor_transferencia
        saldos[conta] = transferencia
        saldos[self.conta] = self.saldo
        print("Operação realizada com sucesso.")
        return True
    

c1 = Banco("Wellington",20,"wellingtonasilva45@gmail.com")
c2 = Banco("Maria",20,"maria123@gmail.com")

c1.cadastro()
c2.cadastro()
      
c1.deposito(1000)
c2.deposito(1000)
    
c1.deposito(500)
        
c1.cadastro()
c2.cadastro()
c1.transferencia(5)
print("contas e saldos")
print()
for chave,item in saldos.items():
    print(chave,item)
print()
c1.cadastro()
c2.cadastro()