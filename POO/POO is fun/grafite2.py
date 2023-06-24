# Faça o modelo de uma lapiseira que pode conter vários grafites.

# Intro
# Iniciar lapiseira
# Inicia uma lapiseira de determinado calibre sem grafite.

# Lapiseiras possuem um bico e um tambor.
# O bico guarda o grafite que está em uso.
# O tambor guarda os grafites reservas.

# Inserir grafite
# Insere um grafite passando
# o calibre: float.
# a dureza: string.
# o tamanho em mm: int.
# Não deve aceitar um grafite de calibre não compatível.
# O grafite é colocado como o ÚLTIMO grafite do tambor.

# Puxar grafite
# Puxa o grafite do tambor para o bico.
# Se já tiver um grafite no bico, esse precisa ser removido primeiro.

# Remover grafite
# Retira o grafite do bico.

# Escrever folha
# Não é possível escrever se não há grafite no bico.
# Quanto mais macio o grafite, mais rapidamente ele se acaba. Para simplificar, use a seguinte regra:
# Grafite HB: 1mm por folha.
# Grafite 2B: 2mm por folha.
# Grafite 4B: 4mm por folha.
# Grafite 6B: 6mm por folha.
# O último centímetro de um grafite não pode ser aproveitado, quando o grafite estiver com 10mm, não é mais possível escrever e o grafite deve ser retirado.
# Se não houver grafite suficiente para terminar a folha, avise que o texto ficou incompleto.

class Lapiseira:

    def __init__(self,calibre,grafite=False):
        self.calibre =  calibre
        self.grafite =  grafite
       
        self.bico = False
        self.tambor = 0
    
    def insere_grafite(self,other):
        if other.calibre != self.calibre:
            print("Lapiseira não aceita esse calibre de grafite.")
            return False
        
        self.tambor += 1
       
        print("Grafite inserido.")
        return True
    
    def puxar_grafite(self,other):
        if self.bico:
            print("Remova primeiro o grafite do bico para poder puxar um grafite do tambor.")
            return False
        
        if self.tambor == 0:
            print("O tambor está vazio, adicione grafites para poder puxar.")
            return False
        
        self.tambor -= 1
        self.bico = True
        self.dureza = other.dureza
        self.tamanho = other.tamanho

        print("O grafite está no bico.")
        return True
    
    def remover_grafite(self):
        if not self.bico:
            print("O bico não tem nenhum grafite para remover.")
            return False
        self.bico = False
        print("O grafite foi removido.")
        return True
    
    def escrever_na_folha(self):
        if not self.bico:
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

class Grafite:

    def __init__(self,calibre,dureza,tamanho):
        self.calibre =  calibre
        self.dureza =  dureza
        self.tamanho =  tamanho


g1 = Grafite(0.7,"macio",11)
g2 = Grafite(0.7,"macio",37)
g3 = Grafite(0.5,"macio",45)
g4 = Grafite(0.7,"macio",45)
g5 = Grafite(0.7,"macio",22)
g6 = Grafite(0.9,"macio",45)
l1 = Lapiseira(0.7)

l1.insere_grafite(g1)
l1.insere_grafite(g2)
l1.insere_grafite(g3)
l1.insere_grafite(g4)
l1.insere_grafite(g5)
l1.insere_grafite(g6)
l1.remover_grafite()
print(l1.tambor)
l1.puxar_grafite(g1)
l1.puxar_grafite(g2)
l1.remover_grafite()
l1.puxar_grafite(g2)
print(l1.tambor)