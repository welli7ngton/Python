import contas


class Pessoa:
    def __init__(self, nome: str, idade: int) -> None:
        self.nome = nome
        self.idade = idade

    @property
    def get_nome(self):
        return self.nome

    @get_nome.setter
    def get_nome(self, nome: str) -> str:
        self.nome = nome

    @property
    def get_idade(self):
        return self.idade

    @get_idade.setter
    def get_idade(self, idade: int) -> int:
        self.idade = idade


class Cliente(Pessoa):
    def __init__(self, nome: str, idade: int):
        super().__init__(nome, idade)
        self.conta: contas.Conta | None = None

    def __repr__(self):
        return f"{self.nome.title()}"


if __name__ == "__main__":
    c1 = Cliente("wellington", 20)
    c2 = Cliente("maria", 19)
    c1.conta = contas.ContaCorrente(111, 222)
    c2.conta = contas.ContaPoupanca(333, 444)
    print(c1.conta)
    print(c2.conta)
    c1.nome = "Wellington Almeida"
    c2.nome = "Maria Helena"
    print(c1)
    print(c2)
