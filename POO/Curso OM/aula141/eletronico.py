from log import LogPrintMixin



class Eletronico:

    def __init__(self,nome):
        self.nome = nome
        self.ligado =  False

    def ligar(self):
        if not self.ligado:
            self.ligado = True
    
    def desligar(self):
        if self.ligado:
            self.ligado = False



class Smartphone(Eletronico, LogPrintMixin):

    def ligar(self):
        super().ligar()

        if self.ligado:
            msg = f"{self.nome} está ligado."
            self.log_success(msg)


    def desligar(self):
        super().desligar()

        if not self.ligado:
            msg = f"{self.nome} está desligado."
            self.log_success(msg)