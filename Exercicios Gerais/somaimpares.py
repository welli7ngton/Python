x = int(input("digite o valor de x: "))
y = int(input("digite o valor de y: "))

soma = 0

if x > y:
    menor = y
    maior = x
else:
    maior = y
    menor = x

intervalo = (maior - menor)

for a in range(0, (intervalo - 1 )):
    if menor > maior or menor == maior:
        break
    else:
        if menor %2 == 0:
            soma += (menor + 1) 
            menor +=1                          
        else:
            menor += 1
                        
print(soma) 

