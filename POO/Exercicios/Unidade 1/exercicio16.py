# 6- Crie uma classe chamada "ContaPoupança" que herda da classe "ContaBancária" (do exercício fácil 4) e possui um 
# atributo de instância "juros" e um método "calcular_juros" que calcula o juros sobre o saldo da conta.

from exercicio4 import ContaBancaria


class ContaPoupanca(ContaBancaria):
    
    def calcular_juros(self):
        if self.saldo < 500:
            self.juros = 3/100
        elif self.saldo == 500 and self.saldo < 750:
            self.juros = 5/100
        elif self.saldo >= 750 and self.saldo < 1000:
            self.juros = 7.5/100
        elif self.saldo >= 1000 and self.saldo < 2000:
            self.juros = 10/100 
        else:
            self.juros = 12/100

        print("O juros atual é:",self.juros*100,"%")


c1 = ContaPoupanca("Wellington")

c1.deposito()
c1.verifica_saldo()
c1.calcular_juros()


