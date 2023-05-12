#Crie uma classe para representar um horario (hora, minuto e segundo). Implemente os 
#metodos para fazer as operacoes de incremento (de segundos) no horario e diferenca
#entre dois horarios.

class horario:
    

    def __init__(self, hora, minuto,segundo):

        self.hora = hora
        self.minuto = minuto
        self.segundo = segundo
        
    def incremento(self,segundos):

        self.segundos = segundos

        hora = self.hora + (self.segundo + segundos) // 3600
        resto = (self.segundo + segundos) % 3600
        minutos = self.minuto + resto // 60
        seg = resto % 60

        print(f"{int(hora + self.hora)}:{int(minutos + self.minuto)}:{int(seg + self.segundo)}")

    def diferenca(self,horario2):
        segundos1 = self.hora * 3600 + self.minuto * 60 + self.segundo
        segundos2 = horario2.hora * 3600 + horario2.minuto * 60 + horario2.segundo

        diferenca = segundos2 - segundos1

        difhora = abs(diferenca)//3600
        difresto = abs(diferenca)%3600
        difmin = difresto//60
        difseg = difresto%60

        print(f"a diferença entre horários é: {difhora}:{difmin}:{difseg}")

        


