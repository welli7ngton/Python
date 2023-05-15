#Faça um programa, com uma função que necessite de três argumentos, e que forneça a soma desses três argumentos
#através de uma função. Seu script também deve fornecer a média dos três números, através de uma segunda função
#que chama a primeira.Função invocando função



def fun1(a1,a2=0,a3=0):
    def fun2(a3,a4=0,a5=0):
        soma = a3 + a4 + a5
        return(soma)
    
    s = fun2(a1, a2, a3)
    media = s/3
    print(f"a soma do numeros é = {s} e a média dos tres numeros é = {media}")

print("digite 3 numeros: ")

a = int(input())    
b = int(input()) 
c = int(input()) 

fun1(a,b,c)






