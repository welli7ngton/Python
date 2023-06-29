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

class Conta:
    _agencias_corrente = [
        {00:...},
        {11:...},
        {22:...},
        {33:...},
        {44:...}        
    ]
    _agencias_poupanca = [
        {55:...},
        {66:...},
        {77:...},
        {88:...},
        {99:...}        
    ]
    def sacar(self,valor_saque,agencia,conta,titular):
        ...



class Pessoa:
    def __init__(self):
        self._nome = None
        self._idade = None

    # getter
    @property
    def nome(self):
        return self._nome.title()

    # getter
    @property
    def idade(self):
       return self._idade 
    # setter
    @nome.setter
    def nome(self,valor):
        self._nome = valor

    # setter
    @idade.setter
    def idade(self,valor):
        self._idade = valor

   
class Cliente(Pessoa):
    ...
 
        

        


