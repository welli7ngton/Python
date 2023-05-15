#Escreva uma função que desenhe uma grade como a seguinte:
#
#        + - - - - + - - - - +
#        |         |         |
#        |         |         |
#        |         |         |
#        |         |         |
#        + - - - - + - - - - +
#        |         |         |
#        |         |         |
#        |         |         |
#        |         |         |
#        + - - - - + - - - - +



def desenha_grade():

    print("+ - - - - " * 2 + "+" )

    for a in range(4):
        print("|"+"         |" *2  )

    print("+ - - - - " * 2 + "+" )

    for b in range(4):
        print("|"+"         |" *2  )

    print("+ - - - - " * 2 + "+" )

desenha_grade()