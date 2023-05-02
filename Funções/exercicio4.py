#3- Faça um programa, com uma função que necessite de três argumentos, e que forneça a soma desses três argumentos.

def somas(arg1,arg2,arg3):

    soma = arg1 + arg2 + arg3

    print(f"a soma dos argumentos é:{soma}")

print("digite os tres argumentos: ")
a1 = float(input())
a2 = float(input())
a3 = float(input())    

somas(a1,a2,a3)

