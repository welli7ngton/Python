# Implemente um sistema de conta bancária. Ele deve possuir um atributo privado do tipo double para armazenar o saldo da 
# conta, que inicia com 0.0 por padrão, e 4 métodos públicos: o método setSaldo, para definir o saldo da conta, o método 
# getSaldo, que retorna o valor do saldo, um método depositar , para acrescentar um valor ao saldo, e um método sacar, 
# para retirar um valor do saldo. Considere que o saldo da conta não pode ser negativo.

class Banco:

    def __init__(self):
        self._saldo = None

    def set_saldo(self,valor_saldo):
        if self._saldo != None:
            print("Operação inválida: saldo_ja_definido")
            return False
        if valor_saldo < 0:
            print("Operação inválida: erro_saldo_não_pode_ser_negativo")
            return False

        self._saldo =  valor_saldo
        print("Operação realizada com sucesso.")
        return True

    def get_saldo(self):
        if self._saldo == None:
            return f"Saldo atual: nao_definido"
        return f"Saldo atual: {self._saldo}"

    def depositar(self,valor_deposito):
        if self._saldo == None:
            print("Operação inválida, saldo não definido.")
            return False

        if valor_deposito < 0:
            print("Operação inválida: erro_valor_deposito_menor_que_zero")
            return False
        
        self._saldo += valor_deposito
        print("Operação realizada com sucesso.")
        return True
    
    def sacar(self,valor_saque):
        if valor_saque > self._saldo:
            print("Saldo insuficiente.")
            return False
        self._saldo -= valor_saque
        print("Operação realizada com sucesso.") 
        return valor_saque

c1 = Banco()

print(c1.get_saldo())
c1.depositar(100)
c1.set_saldo(55.70)
print(c1.get_saldo())
c1.depositar(100)
saque =  c1.sacar(50.70)
print(c1.get_saldo())
c1.set_saldo(550.70)

