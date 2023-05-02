d1 = int(input())
d2 = int(input())
d3 = int(input())
d4 = int(input())
d5 = int(input())

if (d1 + d3 + d5) % 2 != 0:
    r1 = True
else:
    r1 = False

if (d2 + d4) % 2 == 0:
    r2 = True
else:
    r2 = False

if d3 == (d1 + 4):
    r3 = True
else:
    r3 = False
    
if d5 == (d3 + 2):
    r4 = True
else:
    r4 = False
  
if r1 == True and r2 == True and r3 == True and r4 == True:
    print("SIM")
else:
    print("NAO")