n = int(input("digite o valor de n: ")) 
num = n -1 
if n == 0 or n == 1:
    fatorial = 1
else:
    for a in range(0, n):       
        n = n * num      
        num -= 1          
        if num == 0:
            break
print(f"FATORIAL = {n}")