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

        hora = self.segundos // 3600
        resto = self.segundos % 3600
        minutos = resto // 60
        seg = resto % 60

        print(f"{int(hora + self.hora)}:{int(minutos + self.minuto)}:{int(seg + self.segundo)}")

    def diferenca(self,horario2):
        tseg = self.segundo - horario2.segundo
        tmin = self.minuto - horario2.minuto
        thora = self.hora - horario2.hora

        if tseg < 0:
            tseg += 60
            tmin -= 1
        if tmin < 0:
            tmin += 60
            thora -= 1
        if thora < 0:
            thora += 24

        print(f"a diferenca entre as horas é: {int(tseg)}:{int(tmin)}:{int(thora)}")


