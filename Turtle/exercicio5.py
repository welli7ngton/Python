#Escreva um conjunto de funções adequadamente geral que possa desenhar flores como as da Figura 4.1.
#exercicios do livro pense em python
import turtle

q = turtle.Turtle()

def desenhaflor1(b):

    for c in range(2):
        b.rt(45)
        for a in range(8):
            b.lt(3)
            b.fd(30)
            b.lt(6)
        b.lt(150)
        




desenhaflor1(q)
    


turtle.mainloop()