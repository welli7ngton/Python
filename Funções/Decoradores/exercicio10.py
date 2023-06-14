# 10- Escreva uma função decoradora chamada debug que imprima no console os 
# argumentos de entrada e saída de uma função, juntamente com seu nome. Ela 
# deve exibir informações detalhadas para auxiliar na depuração do código.



def debug(funcao):
    def decoradora(*args):
        print(f"Nome da função: {funcao.__name__}")
        print("Argumentos:")
        for arg in args:
            print(f"({arg})",end=" ")
        print('\n')
        print("Sáida da função:")
        print(funcao(*args))
        
    return decoradora
@debug
def calculamedia(nota1,nota2):
    media = 0
    media = (nota1 + nota2) / 2

    return(media)

@debug
def soma(x,y):
    return x+y
@debug
def sub(x,y):
    return x-y
@debug
def div(x,y):
    return x/y
@debug
def prod(x,y):
    return x*y

calculamedia(9,4)
