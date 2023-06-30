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
    def __init__(self, agencia: int, numeracao: int, saldo: float = 0) -> bool:
        super().__init__(agencia, numeracao, saldo)

    def sacar(self, valor_saque: float):
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
            saldo: float = 0,
            limite: float = 0
            ) -> None:
        super().__init__(agencia, numeracao, saldo)
        self.limite = limite

    def sacar(self, valor_saque: float) -> bool:
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


# testes contas
# c1 = ContaCorrente(111, 222, 100, 200)
# c2 = ContaPoupanca(333, 444, 100)


# print(c1)
# print(c2)
# c1.sacar(100)
# c2.detalhes()
# c2.sacar(100)
# c2.depositar(1000)
# c2.sacar(10001)
# c1.sacar(1)
# c1.sacar(100)
# c1.depositar(100)
# c1.depositar(7)


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
                            saldo: float = 0,
                            limite: float = 0
                            ):
        self.conta = ContaCorrente(agencia, numeracao, saldo, limite)

    def cria_conta_poupanca(self,
                            agencia: int,
                            numeracao: int,
                            saldo: float = 0
                            ):
        self.conta = ContaPoupanca(agencia, numeracao, saldo)

    def add_banco_cliente(self):
        ...


# testes clientes com contas
# c1 = Cliente("Wellington", 20)
# c1.cria_conta_corrente(111, 222, 100)
# conta_c1 = c1.conta
# conta_c1.sacar(50)

# c2 = Cliente("Maria Helena", 18)
# c2.cria_conta_poupanca(333, 444, 100)
# conta_c2 = c2.conta
# conta_c2.sacar(50)
# conta_c2.depositar(1000)
# conta_c2.detalhes()
# print(c1)
# print(c2)


class Banco:
    def __init__(self,
                 agencias: list[int] | None,
                 clientes: list[Pessoa] | None,
                 contas: list[Conta] | None
                 ) -> None:
        self.agencias = agencias or []
        self.clientes = clientes or []
        self.contas = contas or []

    def checa_agencia(self, conta):
        ...

    def checa_cliente(self, cliente):
        ...

    def checa_conta(self, agencia):
        ...

    def checa_conta_cliente(self, conta, cliente):
        ...


banco1 = Banco(agencias=[111, 222, 333], clientes=[])
