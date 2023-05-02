#Faça um programa que recebe três números do usuário, e identifica o maior através de uma função e o menor número
#através de outra função.Achar maior e menor número com funções


def maior(n1, n2, n3):
    if n1 > n2 and n1 > n3:
        m = n1
    elif n2 > n3:
        m = n2
    else:
        m = n3

    return(m)

def menor(a, b, c):
    if a < b and a < c:
        me = a
    elif b < c:
        me = b
    else:
        me = c
    return(me)

print("digite tres numeros: ")

num1 = int(input())
num2 = int(input())
num3 = int(input())

maiorn = maior(num1, num2,num3)
menorn = menor(num1, num2, num3)

print(f"o maior é: {maiorn}")
print(f"o menor é: {menorn}")
