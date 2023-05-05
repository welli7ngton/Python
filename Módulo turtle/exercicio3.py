#Faça uma cópia do square e mude o nome para polygon. Acrescente outro parâmetro chamado n e altere o corpo para
#que desenhe um polígono regular de n lados.
#   Dica: os ângulos exteriores de um polígono regular de n lados são 360/n graus.

import turtle

def polig(tamanho,n, q=0):

    q = turtle.Turtle()
    b = q
    for a in range(n):
        q.fd(tamanho)
        
        q.lt(360/n)

    for b in range(n):
        q.lt(36)    
        q.fd(tamanho + 61)
        q.lt(108)
    turtle.mainloop()

t = 100
lados = 5

#t = int(input("digite o tamanho: "))
#lados = int(input("quantidade de lados: "))


polig(t,lados)