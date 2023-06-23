# Grafite 🎥

# Faça o modelo de uma lapiseira que pode conter um único grafite.

# Intro

# Iniciar lapiseira.
    # Inicia uma lapiseira de determinado calibre sem grafite no bico.

# Inserir grafite.
    # Insere um grafite passando
    # o calibre: float.
    # a dureza: string.
    # o tamanho em mm: int.
    # Não deve aceitar um grafite de calibre não compatível.

# Remover grafite.
    # Retira o grafite se houver algum.

# Escrever folha.
    # Não é possível escrever se não há grafite ou o grafite tem tamanho menor ou igual a 10mm.

# Quanto mais macio o grafite, mais rapidamente ele se acaba. Para simplificar, use a seguinte regra:
    # Grafite HB: 1mm por folha.    muito duro
    # Grafite 2B: 2mm por folha.    duro
    # Grafite 4B: 4mm por folha.    médio
    # Grafite 6B: 6mm por folha.    macio

# O último centímetro de um grafite não pode ser aproveitado, quando o grafite estiver com 10mm, não é mais possível escrever.

# Se não houver grafite suficiente para terminar a folha, avise que o texto ficou incompleto.

# Quanto mais macio o grafite, mais rapidamente ele se acaba. Para simplificar, use a seguinte regra:
    # Grafite HB: 1mm por folha.    muito duro
    # Grafite 2B: 2mm por folha.    duro
    # Grafite 4B: 4mm por folha.    médio
    # Grafite 6B: 6mm por folha.    macio

class Lapiseira:

    def __init__(self,calibre=0.0):
        self.calibre = calibre
        self.tem_grafite = False

    def insere_grafite(self,calibre,dureza,tamanho):
        if self.tem_grafite:
            print("A lapiseira ja tem um grafite.")
            return False
        if calibre != self.calibre:
            print("Lapiseira não aceita esse calibre de grafite.")
            return False


        self.calibre = calibre
        self.dureza = dureza.lower()
        self.tamanho = tamanho
        self.tem_grafite = True
        print("Grafite inserido.")
        return True
    
    def remover_grafite(self):
        if self.tem_grafite:
            self.tem_grafite = False
            print("Grafite removido.")
            return True
        
        print("A lapiseira está vazia.")

    def escrever(self):
        if not self.tem_grafite:
            print("Impossível escrever sem grafite na lapiseira.")
            return False
        if self.tamanho <= 10:
            print("Texto incompleto, grafite acabou.")
            return False
        if self.dureza == "muito duro" and self.tamanho >= 11:
            self.tamanho -= 1
            print("Folha escrita.")
            return True
        elif self.dureza == "duro" and self.tamanho >= 12:
            self.tamanho -= 2
            print("Folha escrita.")
            return True
        elif self.dureza == "medio" and self.tamanho >= 14:
            self.tamanho -= 4
            print("Folha escrita.")
            return True
        elif self.dureza == "macio" and self.tamanho >= 16:
            self.tamanho -= 6
            print("Folha escrita.")
            return True
        else:
            print("Não é possível escrever na folha, dureza não definida.")
            return False

# Cria uma lapiseira com calibre 0.5
lapiseira = Lapiseira(0.5)

# Insere um grafite com calibre 0.5, dureza "muito duro" e tamanho 15
lapiseira.insere_grafite(0.5, "muito duro", 15)

# Tenta inserir um novo grafite, deve imprimir a mensagem de que já tem um grafite
lapiseira.insere_grafite(0.5, "duro", 10)

# Tenta escrever uma folha, deve imprimir a mensagem de texto incompleto
lapiseira.escrever()

# Remove o grafite
lapiseira.remover_grafite()

# Tenta escrever uma folha, deve imprimir a mensagem de impossível escrever sem grafite
lapiseira.escrever()
