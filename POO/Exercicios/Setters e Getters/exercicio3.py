# 3- Crie uma classe chamada "BankAccount" com as propriedades nome, conta e interest_rate. Implemente um setter para 
# interest_rate que verifica se o valor passado é um número entre 0 e 1.


class BankAccount:

    def __init__(self,nome,conta):
        self.nome = nome
        self.conta = conta
        

    def set_interest_rate(self,interest_rate):
        self.interest_rate = interest_rate
        if self.interest_rate > 0 and self.interest_rate < 1:
            return True

        return False


c1 = BankAccount("Wellington", "1234-5",) 
c2 = BankAccount("Maria", "1958-5",) 
c3 = BankAccount("Maria", "1958-5",) 


print(c1.set_interest_rate(0.92323145211241231234384449))
print(c2.set_interest_rate(0.9899999999999999998))
print(c3.set_interest_rate(1.0))