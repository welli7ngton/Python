"""
Exercício com Abstração, Herança, Encapsulamento e Polimorfismo
Criar um sistema bancário (extremamente simples) que tem clientes, contas e
um banco. A ideia é que o cliente tenha uma conta (poupança ou corrente) e que
possa sacar/depositar nessa conta. Contas corrente tem um limite extra.

Conta (ABC)
    ContaCorrente
    ContaPoupanca

Pessoa
    Cliente
        Clente -> Conta (um para um ou um para muitos)

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
    Banco tem contas e clientes (Agregação)
    * Checar se a agência é daquele banco
    * Checar se o cliente é daquele banco
    * Checar se a conta é daquele banco
Só será possível sacar se passar na autenticação do banco (descrita acima)
Banco autentica por um método (autenticar).
"""

import abc


class Banco:

    def __init__(self, nome, agencias: list[int]) -> None:
        self.nome = nome
        self.agencias = agencias
        self.contas = []
        self.clientes = []

    def __repr__(self) -> str:
        return f"{__class__.__name__}: {self.nome}"

    def checa_agencia(self, cliente) -> bool:
        if cliente.agencia not in self.agencias:
            False
        True

    def checa_conta(self, cliente) -> bool:
        if cliente.conta not in self.contas:
            return False
        True

    def checa_cliente(self, cliente) -> bool:
        if cliente not in self.clientes:
            return False
        True

    def autenticar(self):
        if not self.checa_agencia or not self.checa_conta:
            return False
        print("Conta autenticada.")
        return True


class Pessoa:
    def __init__(self, nome: str, idade: int) -> None:
        self.nome = nome
        self.idade = idade

    @property
    def get_nome(self):
        return self.nome

    @get_nome.setter
    def get_nome(self, valor: str):
        self.nome = valor

    @property
    def get_idade(self):
        return self.idade

    @get_idade.setter
    def get_idade(self, valor: int):
        self.idade = valor


class Cliente(Pessoa):

    def __init__(self, nome: str, idade: int) -> None:
        super().__init__(nome, idade)
        self.banco = None

    def __repr__(self) -> str:
        print(f"Dados do cliente: {self.nome}")
        return f"Agência: {self.conta.agencia}\
            \nNumeração: {self.conta.numeracao}"

    def cria_conta_corrente(self,
                            agencia: int,
                            numeracao: int,
                            banco: Banco,
                            saldo: float = 0,
                            limite: float = 0
                            ):
        if agencia not in banco.agencias:
            print("Nosso banco não contém essa agencia, operação cancelada.")
            return False
        self.conta = ContaCorrente(agencia, numeracao, banco, saldo, limite)
        self.banco = banco
        self.banco.contas.append(numeracao)

    def cria_conta_poupanca(self,
                            agencia: int,
                            numeracao: int,
                            banco: Banco,
                            saldo: float = 0
                            ):
        if agencia not in banco.agencias:
            print("Nosso banco não contém essa agencia, operação cancelada.")
            return False
        self.conta = ContaPoupanca(agencia, numeracao, banco, saldo)
        self.banco.contas.append(numeracao)


class Conta(abc.ABC):
    def __init__(self, agencia: int, numeracao: int, saldo: float = 0) -> None:
        self.agencia = agencia
        self.numeracao = numeracao
        self.saldo = saldo

    @abc.abstractclassmethod
    def sacar(self, valor_saque: float):
        pass

    def __repr__(self) -> str:
        return f"Agencia({self.agencia!r}) | Numeração({self.numeracao!r})"

    def detalhes(self, msg: str = "Detalhes:"):
        print(msg, "\n", f"Saldo atual: {self.saldo:.2f}")


class ContaPoupanca(Conta):
    def __init__(self,
                 agencia: int,
                 numeracao: int,
                 banco: Banco,
                 saldo: float = 0
                 ) -> bool:
        super().__init__(agencia, numeracao, saldo)
        self.banco = banco

    def sacar(self, valor_saque: float):
        print("Autenticando...")
        if not self.banco.autenticar():
            return False
        if self.saldo < valor_saque:
            self.detalhes(msg="Operação não realizada, saldo insuficiente.")
            return False
        self.saldo -= valor_saque
        self.detalhes(msg="Operação realizada.")
        return True

    def depositar(self, valor_deposito: float) -> bool:
        self.saldo += valor_deposito
        self.detalhes(msg="Operação realizada.")
        return True


class ContaCorrente(Conta):
    def __init__(
            self,
            agencia: int,
            numeracao: int,
            banco: Banco,
            saldo: float = 0,
            limite: float = 0
            ) -> None:
        super().__init__(agencia, numeracao, saldo)
        self.limite = limite
        self.banco = banco
        print(self.banco)

    def sacar(self, valor_saque: float) -> bool:
        print("Autenticando...")
        if not self.banco.autenticar():
            return False
        valor_pos_saque = self.saldo - valor_saque
        limite_maximo = -self.limite

        if valor_pos_saque <= limite_maximo:
            self.detalhes(msg="Operação não realizada, limite insuficiente.")
            return False
        self.saldo -= valor_saque
        self.detalhes(msg="Operação realizada.")

    def depositar(self, valor_deposito: float) -> bool:
        self.saldo += valor_deposito
        self.detalhes(msg="Operação realizada.")
        return True


banco1 = Banco("Nubank", [111, 222, 333])
banco2 = Banco("Picpay", [444, 555, 666])

cliente1 = Cliente("Wellington", 20)
cliente2 = Cliente("Maria Helena", 20)

conta_corrente1 = cliente1.cria_conta_corrente(112, 10, banco1, 100, 50)
cliente1.cria_conta_corrente(111, 10, banco1, saldo=100, limite=50)
print(cliente1.conta)
cliente1.conta.sacar(100)
