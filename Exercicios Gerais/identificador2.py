d1 = int(input())
d2 = int(input())
d3 = int(input())
d4 = int(input())
d5 = int(input())

if d3 == (d1 + d2):
    r1 = True
else:
    r1 = False
    
if d4 % 2 == 0:
    d4 = 2*d2
    if d4 % 2 == 0:
        r2 = True
    else:
        r2 = False
    
else:
    d4 = 2*d2 + 1
    if d4 % 2 == 0:
        r2 = True
    else:
        r2 = False


if d5 % d3 == 0:
    d5 = 2*d3
    if d5 % d3 == 0:
        r3 = True
    else:
        r3 = False
        
        
else:
    d5 = 2*d3 - 1    
    if d5 % d3 == 0:  
        r3 = True
    else:
        r3 = False

    
if r1 == True and r2 == True and r3 == True:
    print("SIM")
else:
    print("NAO")




#d3 = d1 + d2;   ok
#Se d4 for par então d4 = 2*d2, caso contrário d4 = 2*d2 + 1;   ok
#Se d5 for divisível por d3 então d5 = 2*d3 caso contrário d5 = 2*d3 - 1.   
