#Crie uma classe para representar um numero complexo. Implemente, usando sobrecarga 
#de operador, os metodos para fazer as operacoes de soma, subtracao e produto entre 
#dois numeros


class num_complexo:

    def __init__(self):
        self.num1 = int(input("digite num1: "))
        self.num2 = int(input("digite num2: "))
        return
    
    def operacoes(self):

        som = self.num1 + self.num2
        sub = self.num1 - self.num2
        prod = self.num1 * self.num2

        return (som, sub, prod)
    

    
  