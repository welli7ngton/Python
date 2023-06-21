# Porquinho

# O sistema deverá:

# Gerenciar um cofrinho do tipo Porquinho capaz de guardar moedas e itens.
# As moedas devem ser criadas através de uma enum.
# Ambos moedas e itens tem um método getVolume() e getLabel().
# O volume do cofre incrementa conforme ele recebe itens e moedas.
# A lógica da utilização do cofre é:
# Para inserir moedas e itens o cofre deve estar inteiro.
# Para extrair moedas e itens o cofre deve estar quebrado.
# Ao quebrar, o volume do porco deve ser zerado e o status de broken deve ser alterado para true.
# Ao extrair moedas e itens, os atribuitos valor e itens devem se tornar listas vazias.

import random

class Porquinho:

    sorte = [1,2,3,7,4,5,6]

    def __init__(self):
        print("O cofre está pronto para ser usado!")
        self.volume = 0
        self.broken = False
        self.valores_moedas = []
        self.items = []

    def add_moeda(self,valor_moeda):
        if self.broken == True:
            print("O cofre está quebrado.")    
            return False 
        if valor_moeda > 1.0:
            print("Coloque uma moeda por vez.")
            return False
        self.volume += 1
        self.valores_moedas.append(valor_moeda)
        print("Moeda adicionada ao cofre.")
    
    def add_item(self,item):
        if self.broken == True:
            print("O cofre está quebrado.")    
            return False 
        self.items.append(item)
        self.volume += 2
        print("Item adicionado ao cofre.")

    def quebrar_cofre(self):
        if self.broken == True:
            print("O cofre está quebrado.")    
            return False 
        self.broken = True
        self.valores_moedas = []
        self.items = []
        self.volume = 0
        print("O cofre está quebrado.")
    
    def verifica_volume(self):
        if self.broken == True:
            print("O cofre está quebrado.")    
            return False 
        print(f"O Volume do cofre atualmente é: {self.volume}.")
    
    def verifica_valor(self,sorte=sorte):
        if self.broken == True:
            print("O cofre está quebrado.")    
            return False 
        indice = random.randint(0,6)
        if sorte[indice] == 7:
            print("Você está com sorte :D")
            print(f"Valor cofre: R${sum(self.valores_moedas):.2f}")
            return True
        print("Você está com azar :p")
        return False
    

p1 = Porquinho()  
p1.add_moeda(1.0) 
p1.add_moeda(0.25) 
p1.add_moeda(1.0) 
p1.add_moeda(0.5) 
p1.add_moeda(1.5) 
p1.add_moeda(1.0) 
p1.add_moeda(0.25) 
p1.add_moeda(.10) 
p1.verifica_valor()
p1.quebrar_cofre()
p1.add_moeda(.10) 
p1.add_moeda(1.0) 