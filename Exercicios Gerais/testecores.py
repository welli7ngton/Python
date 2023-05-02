for a in range(0, 10):
    if a %2 == 0:

        print(f" -> \033[32m {a}",end="")
    else:
        print(f" -> \033[31m {a}",end="")