# Calculadora
# O objetivo dessa atividade é implementar uma calculadora a bateria. Se há bateria, ela executa operações de soma, multiplicação e divisão. É possível também mostrar a quantidade de bateria e recarregar a calculadora. Ela avisa quando está sem bateria e se há tentativa de divisão por 0.

# Intro
# Mostrar bateria da calculadora.
# Recarregar a bateria.
# Realizar operações matemáticas de soma e divisão.
# Se o usuário tentar realizar operações e a bateria estiver vazia, deverá ser mostrada uma notificação sobre falta de bateria.
# Se for tentada divisão por zero, deve ser notificado o erro.
import time
class Calculadora:

    def __init__(self):
        self.bateria = 100

    def soma(self,x,y):
        if self.bateria > 0:                
            print(x+y)
            self.bateria -= 10
        else:
            print("Bateria insuficiente, recarregue para poder usar a calculadora.")

    def divisao(self,x,y):
        if self.bateria > 0:
            try:
                print(x/y)
                self.bateria -= 10
            except ZeroDivisionError:
                self.bateria -= 15
                print("Não é possível dividir por 0.")
        else:
            print("Bateria insuficiente, recarregue para poder usar a calculadora.")      
    def status_bateria(self):
        print(f"O nível atual da bateria é: {self.bateria}%")

    def recarregar(self):
        print("Recarregando...")
        if self.bateria < 0:
            self.bateria = 0
        while True:
            print(f"{self.bateria}%")
            self.bateria += 10 if self.bateria < 100 else 0
            time.sleep(2)
            print("Recarregando...")
            if self.bateria >= 100:
                self.bateria -= (self.bateria - 100)
                print("Bateria 100% carregada.")
                break
c1 = Calculadora()

c1.soma(2,2)
c1.soma(2,2)
c1.soma(2,2)
c1.soma(2,2)
c1.status_bateria()
c1.soma(2,2)
c1.soma(2,2)
c1.soma(2,2)
c1.status_bateria()
c1.soma(2,2)
c1.recarregar()
c1.status_bateria()
c1.soma(2,2)
c1.soma(2,2)
c1.status_bateria()
c1.divisao(15,3)
c1.divisao(15,3)
c1.divisao(15,0)
c1.divisao(15,0)
c1.divisao(15,0)
c1.recarregar()
c1.status_bateria()
c1.divisao(15,3)
c1.status_bateria()
c1.divisao(15,3)