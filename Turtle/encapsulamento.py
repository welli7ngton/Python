import turtle

bob = turtle.Turtle()


def quadrado(t, tamanho):
    for i in range(4):
        t.fd(tamanho)
        t.lt(90)    
    
quadrado(bob,200)

turtle.mainloop()