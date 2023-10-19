print("digite os valores de x e y: ")
x = int(input())
y = int(input())


while x != 0 and y != 0:
    if x > 0 and y > 0:
        print("quadrante 1")
    elif x > 0 and y < 0:
        print("quadrante 4")
    elif x < 0 and y < 0:
        print("quadrante 3")
    elif x < 0 and y > 0:
        print("quadrante 2")

    print("digite os valores de x e y: ")
    x = int(input())
    y = int(input())






