num = int(input("deseja a tabela de qual numero? "))
cont = 1
for a in range(0, 9):
    result = num*cont
    print(f"{num} x {cont} = {result}")
    cont += 1
