tam = int(input())

l1 = [0 for x in range(tam)]
l2 = [0 for x in range(tam)]

for a in range(0,len(l1)):
    l1[a] = int(input())

for a in range(0,len(l2)):
    l2[a] = int(input())

for a in range(0, len(l1)):
    if a %2 == 0:
        l1[a], l2[a] = l2[a], l1[a]
        
print(l1)
print(l2)