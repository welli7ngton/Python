#Acrescente outro parâmetro, chamado length, ao square. Altere o corpo para que o comprimento dos lados seja
#length e então altere a chamada da função para fornecer um segundo argumento. Execute o programa novamente. Teste
#o seu programa com uma variedade de valores para length.


import turtle

def quadrado(tamanho, q=0):

    q = turtle.Turtle()
    for a in range(4):
        q.fd(tamanho)
        q.lt(90)
    
    turtle.mainloop()



t = int(input("digite o tamanho do quadrado: "))

quadrado(t)
