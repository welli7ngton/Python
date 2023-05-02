x = int(input("digite o valor de x: "))
num = 0

if x %2 == 0:

    y = x - 2

    for a in range(1,x):

        num = x - y
        y -= 1
        if num %2 != 0:
            print(num)
else:

    y = x - 1

    for a in range(0,x):

        num = x - y
        y -= 1
        if num %2 != 0:
            print(num)


        