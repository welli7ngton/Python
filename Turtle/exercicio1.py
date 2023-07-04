#Escreva uma função chamada square que receba um parâmetro chamado t, que é um turtle. Ela deve usar o turtle para 
#desenhar um quadrado.

#Escreva uma chamada de função que passe bob como um argumento para o square e então execute o programa novamente



import turtle

def teste(bob=0):

    bob = turtle.Turtle()

    for i in range(4):

        bob.fd(100)
        bob.lt(90)

    turtle.mainloop()

teste()
