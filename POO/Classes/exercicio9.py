#9. Um racional é qualquer numero da forma p/q, sendo p inteiro e q inteiro nao nulo. Crie
#uma classe para representar um racional e os seguinte metodos: 
#(a) inverter sinal;
#(b) somar dois racionais;
#(c) subtrair dois racionais;
#(d) produto de dois racionais;
#(e) quociente de dois racionais;
import math

class racional:

    def __init__(self,num, den):
        self.num = num
        self.den = den
           
    def inverte_sinal(self):
        self.num *= -1
          
    def soma(self,outro):
        mmc = self.den * outro.den // math.gcd(self.den, outro.den)
        novo_num = self.num * (mmc//self.den) + outro.num *(mmc//outro.den)
        novo_den = mmc
        n = novo_num//math.gcd(novo_num, novo_den)
        d = novo_den//math.gcd(novo_num, novo_den) 
        return(n,d)

    def sub(self, outro):
        mmc = self.den * outro.den // math.gcd(self.den, outro.den)
        novo_num = self.num * (mmc//self.den) - outro.num*(mmc//outro.den)
        novo_den = mmc
        n = novo_num//math.gcd(novo_num, novo_den)
        d = novo_den//math.gcd(novo_num, novo_den) 
        return(n,d)

    def produto(self,outro):
        novo_num = self.num * outro.num
        novo_den = self.den * outro.den
        n = novo_num // math.gcd(novo_num, novo_den)
        d = novo_den // math.gcd(novo_num, novo_den)
        return(n,d)
    
    def divisao(self, outro):
        novo_num = self.num * outro.den
        novo_den = self.den * outro.num
        n = novo_num // math.gcd(novo_num, novo_den)
        d = novo_den // math.gcd(novo_num, novo_den)
        return(n,d)
        




        


    

        