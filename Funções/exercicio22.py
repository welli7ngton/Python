#Ordene um	 vetor	 de	 100	 números	 inteiros	 gerados	 aleatoriamente.	 Esse	 programa	
#deve	 implementar	 o	 algoritmo	 selection	 sort.	 Esse	 algoritmo	 faz	 uso	 de	 uma função	
#para	selecionar	o	menor	elemento	a	partir	de	cada	posição	do	vetor	e	inseri-lo nesta
#posição. Não	utilize	a	função	sort	do	Python.


import random


def geravetor():

    vet1 = []

    for a in range(100):
        vet1.append(random.randrange(0,101))

    return vet1

def organiza(vet):

    for a in range(len(vet)):
        menor = a
        for b in range(a + 1, len(vet)):
            if vet[b] < vet[menor]:
                menor = b

        vet[a], vet[menor]   = vet[menor], vet[a]       


    return vet
        
vetor = geravetor()
vetoro = organiza(vetor)

print(vetoro)


