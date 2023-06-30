"""
Exercício com Abstração, Herança, Encapsulamento e Polimorfismo
Criar um sistema bancário (extremamente simples) que tem clientes, contas e
um banco. A ideia é que o cliente tenha uma conta (poupança ou corrente) e que
possa sacar/depositar nessa conta. Contas corrente tem um limite extra.
Conta (ABC)
    ContaCorrente
    ContaPoupanca
Pessoa (ABC)
    Cliente
        Clente -> Conta
Banco
    Banco -> Cliente
    Banco -> Conta
Dicas:
Criar classe Cliente que herda da classe Pessoa (Herança)
    Pessoa tem nome e idade (com getters)
    Cliente TEM conta (Agregação da classe ContaCorrente ou ContaPoupanca)
Criar classes ContaPoupanca e ContaCorrente que herdam de Conta
    ContaCorrente deve ter um limite extra
    Contas têm agência, número da conta e saldo
    Contas devem ter método para depósito
    Conta (super classe) deve ter o método sacar abstrato (Abstração e
    polimorfismo - as subclasses que implementam o método sacar)
Criar classe Banco para AGREGAR classes de clientes e de contas (Agregação)
Banco será responsável autenticar o cliente e as contas da seguinte maneira:
    Banco tem contas e clentes (Agregação)
    * Checar se a agência é daquele banco
    * Checar se o cliente é daquele banco
    * Checar se a conta é daquele banco
Só será possível sacar se passar na autenticação do banco (descrita acima)
Banco autentica por um método.
"""


from abc import ABC, abstractmethod


class Conta(ABC):
    def __init__(self, agencia, numero, saldo=0):
        self.agencia = agencia
        self.numero = numero
        self.saldo = saldo

    @abstractmethod
    def sacar(self, valor_saque): ...

    def detalhes(self, msg=""):
        print(msg, f"Seu saldo atual é: {self.saldo:.2f}")

    def depositar(self, valor_deposito):
        self.saldo += valor_deposito
        self.detalhes(msg="Operação realizada.\n")
        return True


class ContaPoupanca(Conta):
    def __init__(self, agencia, numero, saldo=0):
        self.agencia = agencia
        self.numero = numero
        self.saldo = saldo

    def __repr__(self) -> str:
        return f"Agencia({self.agencia}) | Numero({self.numero})"

    def sacar(self, valor_saque):
        if valor_saque > self.saldo:
            self.detalhes(msg="Saldo insuficiente, operação não realizada.\n")
            return False
        self.saldo -= valor_saque 
        self.detalhes(msg="Operação realizada.\n")
        return True


class ContaCorrente(Conta):
    def __init__(self, agencia, numero, saldo=0, limite=0):
        super().__init__(agencia, numero, saldo)
        self.limite = limite

    def __repr__(self) -> str:
        return f"Agencia({self.agencia}) | Numero({self.numero})"

    def sacar(self, valor_saque):
        valor_pos_saque = self.saldo - valor_saque
        limite_maximo = -self.limite

        if valor_pos_saque >= limite_maximo:
            self.saldo -= valor_saque
            self.detalhes(msg="Operação realizada.\n")
            return True

        self.detalhes(msg="Operação não realizada.\n")
        return False   
# testes

# cp1 = ContaPoupanca(111,222,100)
# cp1.sacar(200)
# cp1.sacar(99)
# cp1.depositar(1000)
# cp1.sacar(1001)
# cp1.sacar(1)

# cc1 = ContaCorrente(111,222,100,100)
# cc1.sacar(1)
# cc1.depositar(1)
# cc1.sacar(100)
# cc1.sacar(100)
# cc1.sacar(100)
# cc1.depositar(50)
# cc1.sacar(100)
# cc1.depositar(50)
# cc1.depositar(100)
